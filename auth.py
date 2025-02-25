# auth.py
from config import USERS

def authenticate(username: str, password: str) -> bool:
    """Check if the username and password are valid."""
    return USERS.get(username) == password
