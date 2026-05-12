import hashlib
import secrets
from cryptography.fernet import Fernet

class Security:
    """Security utilities"""
    
    @staticmethod
    def hash_password(password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password, hash_value):
        """Verify password against hash"""
        return Security.hash_password(password) == hash_value
    
    @staticmethod
    def generate_token(length=32):
        """Generate secure random token"""
        return secrets.token_hex(length // 2)
    
    @staticmethod
    def encrypt_message(message, key):
        """Encrypt message using Fernet"""
        f = Fernet(key)
        return f.encrypt(message.encode()).decode()
    
    @staticmethod
    def decrypt_message(encrypted, key):
        """Decrypt message using Fernet"""
        f = Fernet(key)
        return f.decrypt(encrypted.encode()).decode()
    
    @staticmethod
    def is_secure_token(token):
        """Check if token format is secure"""
        return len(token) >= 32 and all(c in '0123456789abcdef' for c in token)

__all__ = ["Security"]
