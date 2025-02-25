# proxy_server.py
import socket
import asyncio
import logging
from encryption import encrypt, decrypt
from auth import authenticate
from config import PROXY_HOST, PROXY_PORT, MAX_CLIENTS

# Setup logging
logging.basicConfig(filename='logs/proxy.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    logging.info(f'New connection from {addr}')
    print(f'Connection from {addr}')

    try:
        # Receive client data
        data = await reader.read(1024)

        # Check if it's an HTTP CONNECT request
        if data.startswith(b"CONNECT "):
            print("Received CONNECT request, setting up tunnel...")

            # Extract the destination host and port
            request_line = data.decode('utf-8').split("\r\n")[0]
            _, host_port, _ = request_line.split(" ")
            dest_host, dest_port = host_port.split(":")
            dest_port = int(dest_port)

            # Connect to the target server
            remote_reader, remote_writer = await asyncio.open_connection(dest_host, dest_port)
            print(f'Connected to {dest_host}:{dest_port} ✅')

            # Send a success response back to the client
            writer.write(b"HTTP/1.1 200 Connection Established\r\n\r\n")
            await writer.drain()

            # Forward data between client and destination
            async def forward_data(src_reader, dest_writer):
                try:
                    while True:
                        data = await src_reader.read(1024)
                        if not data:
                            break
                        dest_writer.write(data)
                        await dest_writer.drain()
                except Exception as e:
                    logging.error(f'Data forwarding error: {e}')

            # Run bidirectional forwarding
            await asyncio.gather(
                forward_data(reader, remote_writer),
                forward_data(remote_reader, writer)
            )
            return

        # If not a CONNECT request, proceed with normal authentication
        decrypted_data = decrypt(data).decode('utf-8')

        username, password = decrypted_data.split(":")
        if not authenticate(username, password):
            print(f'Authentication failed for {addr} ❌')
            logging.error(f'Authentication failed for {addr} ❌')
            writer.close()
            await writer.wait_closed()
            return

        print(f'User {username} authenticated successfully. ✅')
        logging.info(f'User {username} authenticated successfully. ✅')

    except Exception as e:
        logging.error(f'Error handling client {addr}: {e}')
        print(f'Error: {e}')

    finally:
        writer.close()
        await writer.wait_closed()
        logging.info(f'Connection closed from {addr}')
        print(f'Connection closed from {addr}')


async def main():
    server = await asyncio.start_server(handle_client, PROXY_HOST, PROXY_PORT)
    logging.info(f'SOCKS5 Proxy Server started on {PROXY_HOST}:{PROXY_PORT}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
