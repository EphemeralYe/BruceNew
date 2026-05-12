from .base import SessionLocal
from .models import User
from logger import logger
from datetime import datetime

class UserService:
    """User database operations"""
    
    @staticmethod
    def add_user(user_id, username=None, first_name=None, last_name=None):
        """Add or update user in database"""
        try:
            db = SessionLocal()
            user = db.query(User).filter(User.user_id == user_id).first()
            
            if user:
                user.last_seen = datetime.utcnow()
                if username:
                    user.username = username
                if first_name:
                    user.first_name = first_name
            else:
                user = User(
                    user_id=user_id,
                    username=username,
                    first_name=first_name,
                    last_name=last_name
                )
                db.add(user)
            
            db.commit()
            db.close()
            return True
        except Exception as e:
            logger.error(f"Error adding user {user_id}: {e}")
            return False
    
    @staticmethod
    def get_user(user_id):
        """Get user by ID"""
        try:
            db = SessionLocal()
            user = db.query(User).filter(User.user_id == user_id).first()
            db.close()
            return user
        except Exception as e:
            logger.error(f"Error getting user {user_id}: {e}")
            return None
    
    @staticmethod
    def ban_user(user_id):
        """Ban a user"""
        try:
            db = SessionLocal()
            user = db.query(User).filter(User.user_id == user_id).first()
            if user:
                user.is_banned = True
                db.commit()
            db.close()
            return True
        except Exception as e:
            logger.error(f"Error banning user {user_id}: {e}")
            return False
    
    @staticmethod
    def get_all_users():
        """Get all users"""
        try:
            db = SessionLocal()
            users = db.query(User).all()
            db.close()
            return users
        except Exception as e:
            logger.error(f"Error getting all users: {e}")
            return []
    
    @staticmethod
    def get_user_count():
        """Get total user count"""
        try:
            db = SessionLocal()
            count = db.query(User).count()
            db.close()
            return count
        except Exception as e:
            logger.error(f"Error counting users: {e}")
            return 0

__all__ = ["UserService"]
