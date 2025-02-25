import socket
from encryption import encrypt

def send_encrypted_data(username, password):
    """Encrypt and send user credentials to the SOCKS5 proxy."""
    try:
        # Connect to the proxy server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 1080))
        
        # Encrypt the username and password using AES-256
        message = f"{username}:{password}".encode('utf-8')
        encrypted_message = encrypt(message)

        # Send encrypted data
        s.send(encrypted_message)
        print("✅ Encrypted data sent successfully!")

        # Close the connection
        s.close()
    except Exception as e:
        print(f"❌ Error sending data: {e}")

# Example usage
if __name__ == "__main__":
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    send_encrypted_data(username, password)
