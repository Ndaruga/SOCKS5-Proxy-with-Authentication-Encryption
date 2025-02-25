# config.py
PROXY_HOST = '0.0.0.0'  # Bind to all network interfaces
PROXY_PORT = 1080       # Standard SOCKS5 port
MAX_CLIENTS = 100       # Max simultaneous connections

# AES-256 encryption key (32 bytes)
ENCRYPTION_KEY = b'12345678901234567890123456789012'
ENCRYPTION_IV = b'1234567890123456'

# User credentials (username: password)
USERS = {
    'user1': 'password123',
    'admin': 'securepass456'
}