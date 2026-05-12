from database import UserService as UserDB
from logger import logger

class UserManager:
    """User management business logic"""
    
    @staticmethod
    def register_user(user_id, username=None, first_name=None, last_name=None):
        """Register a new user"""
        try:
            success = UserDB.add_user(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name
            )
            if success:
                logger.info(f"User registered: {user_id}")
            return success
        except Exception as e:
            logger.error(f"Error registering user: {e}")
            return False
    
    @staticmethod
    def get_user_info(user_id):
        """Get user information"""
        return UserDB.get_user(user_id)
    
    @staticmethod
    def ban_user(user_id):
        """Ban a user"""
        success = UserDB.ban_user(user_id)
        if success:
            logger.info(f"User banned: {user_id}")
        return success
    
    @staticmethod
    def get_total_users():
        """Get total user count"""
        return UserDB.get_user_count()

__all__ = ["UserManager"]
