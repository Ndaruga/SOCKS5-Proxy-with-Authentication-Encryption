# encryption.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from config import ENCRYPTION_KEY, ENCRYPTION_IV


def encrypt(data: bytes) -> bytes:
    """Encrypt data using AES-256."""
    cipher = Cipher(algorithms.AES(ENCRYPTION_KEY), modes.CFB(ENCRYPTION_IV), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()


def decrypt(data: bytes) -> bytes:
    """Decrypt data using AES-256."""
    cipher = Cipher(algorithms.AES(ENCRYPTION_KEY), modes.CFB(ENCRYPTION_IV), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()
