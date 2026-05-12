from database import UserService
from config import OWNER_ID
from logger import logger

class AuthMiddleware:
    """Authentication and authorization checks"""
    
    @staticmethod
    async def check_user_permission(user_id, required_role="user"):
        """Check user permission level"""
        try:
            user = UserService.get_user(user_id)
            
            if user.is_banned:
                return False
            
            if required_role == "owner":
                return user_id == OWNER_ID
            elif required_role == "admin":
                return user_id == OWNER_ID or user.is_admin
            else:
                return True
        except Exception as e:
            logger.error(f"Error checking permission: {e}")
            return False
    
    @staticmethod
    async def is_owner(user_id):
        """Check if user is owner"""
        return user_id == OWNER_ID
    
    @staticmethod
    async def is_admin(user_id):
        """Check if user is admin"""
        try:
            user = UserService.get_user(user_id)
            return user and user.is_admin
        except:
            return False
    
    @staticmethod
    async def is_banned(user_id):
        """Check if user is banned"""
        try:
            user = UserService.get_user(user_id)
            return user and user.is_banned
        except:
            return False

__all__ = ["AuthMiddleware"]
