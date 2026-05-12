import re

class Validators:
    """Data validation utilities"""
    
    @staticmethod
    def is_valid_chat_id(chat_id):
        """Validate chat ID format"""
        return isinstance(chat_id, int) and chat_id != 0
    
    @staticmethod
    def is_valid_user_id(user_id):
        """Validate user ID format"""
        return isinstance(user_id, int) and user_id > 0
    
    @staticmethod
    def is_valid_file_id(file_id):
        """Validate file ID format"""
        return isinstance(file_id, str) and len(file_id) > 0
    
    @staticmethod
    def is_valid_username(username):
        """Validate Telegram username format"""
        pattern = r'^[a-zA-Z0-9_]{5,32}$'
        return re.match(pattern, username) is not None
    
    @staticmethod
    def is_valid_email(email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def is_safe_filename(filename):
        """Check if filename is safe"""
        dangerous_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        return not any(char in filename for char in dangerous_chars)
    
    @staticmethod
    def is_valid_mime_type(mime_type):
        """Validate MIME type format"""
        pattern = r'^[a-zA-Z]+/[a-zA-Z0-9\-\+\.]*$'
        return re.match(pattern, mime_type) is not None

__all__ = ["Validators"]
