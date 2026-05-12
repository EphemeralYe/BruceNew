from .base import SessionLocal
from .models import FilterIndex
from logger import logger

class IAFilterService:
    """IA filter index database operations"""
    
    @staticmethod
    def add_filter(chat_id, keyword, file_id, file_name):
        """Add filter entry for search"""
        try:
            db = SessionLocal()
            filter_entry = FilterIndex(
                chat_id=chat_id,
                keyword=keyword.lower(),
                file_id=file_id,
                file_name=file_name
            )
            db.add(filter_entry)
            db.commit()
            db.close()
            return True
        except Exception as e:
            logger.error(f"Error adding filter: {e}")
            return False
    
    @staticmethod
    def search_filters(keyword, limit=10):
        """Search filters by keyword"""
        try:
            db = SessionLocal()
            results = db.query(FilterIndex).filter(
                FilterIndex.keyword.ilike(f"%{keyword.lower()}%")
            ).limit(limit).all()
            db.close()
            return results
        except Exception as e:
            logger.error(f"Error searching filters: {e}")
            return []
    
    @staticmethod
    def get_filters_by_chat(chat_id):
        """Get all filters for a chat"""
        try:
            db = SessionLocal()
            filters = db.query(FilterIndex).filter(FilterIndex.chat_id == chat_id).all()
            db.close()
            return filters
        except Exception as e:
            logger.error(f"Error getting filters for chat {chat_id}: {e}")
            return []
    
    @staticmethod
    def delete_filter(filter_id):
        """Delete a filter entry"""
        try:
            db = SessionLocal()
            filter_entry = db.query(FilterIndex).filter(FilterIndex.id == filter_id).first()
            if filter_entry:
                db.delete(filter_entry)
                db.commit()
            db.close()
            return True
        except Exception as e:
            logger.error(f"Error deleting filter {filter_id}: {e}")
            return False

__all__ = ["IAFilterService"]
