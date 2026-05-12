from telethon import events
from config import OWNER_ID
from database import UserService

class Filters:
    """Custom filters for handlers"""
    
    @staticmethod
    def owner_filter(event):
        """Filter for owner only"""
        return event.sender_id == OWNER_ID
    
    @staticmethod
    def not_banned(event):
        """Filter to exclude banned users"""
        user = UserService.get_user(event.sender_id)
        return user and not user.is_banned if user else True
    
    @staticmethod
    def is_group(event):
        """Filter for group messages"""
        return not event.is_private
    
    @staticmethod
    def is_private(event):
        """Filter for private messages"""
        return event.is_private
    
    @staticmethod
    def has_document(event):
        """Filter for messages with documents"""
        return event.document is not None

__all__ = ["Filters"]
