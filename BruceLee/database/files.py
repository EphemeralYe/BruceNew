from .base import SessionLocal
from .models import FileMetadata
from logger import logger

class FileService:
    """File metadata database operations"""
    
    @staticmethod
    def add_file(file_id, file_name, file_size, mime_type, uploader_id, chat_id):
        """Add file metadata to database"""
        try:
            db = SessionLocal()
            file_meta = FileMetadata(
                file_id=file_id,
                file_name=file_name,
                file_size=file_size,
                mime_type=mime_type,
                uploader_id=uploader_id,
                chat_id=chat_id
            )
            db.add(file_meta)
            db.commit()
            db.close()
            return True
        except Exception as e:
            logger.error(f"Error adding file {file_name}: {e}")
            return False
    
    @staticmethod
    def get_file(file_id):
        """Get file metadata by file ID"""
        try:
            db = SessionLocal()
            file_meta = db.query(FileMetadata).filter(FileMetadata.file_id == file_id).first()
            db.close()
            return file_meta
        except Exception as e:
            logger.error(f"Error getting file {file_id}: {e}")
            return None
    
    @staticmethod
    def search_files(query, limit=10):
        """Search files by name"""
        try:
            db = SessionLocal()
            results = db.query(FileMetadata).filter(
                FileMetadata.file_name.ilike(f"%{query}%"),
                FileMetadata.is_deleted == False
            ).limit(limit).all()
            db.close()
            return results
        except Exception as e:
            logger.error(f"Error searching files: {e}")
            return []
    
    @staticmethod
    def delete_file(file_id):
        """Soft delete file"""
        try:
            db = SessionLocal()
            file_meta = db.query(FileMetadata).filter(FileMetadata.file_id == file_id).first()
            if file_meta:
                file_meta.is_deleted = True
                db.commit()
            db.close()
            return True
        except Exception as e:
            logger.error(f"Error deleting file {file_id}: {e}")
            return False
    
    @staticmethod
    def get_files_by_chat(chat_id, limit=50):
        """Get files uploaded in a chat"""
        try:
            db = SessionLocal()
            files = db.query(FileMetadata).filter(
                FileMetadata.chat_id == chat_id,
                FileMetadata.is_deleted == False
            ).limit(limit).all()
            db.close()
            return files
        except Exception as e:
            logger.error(f"Error getting files for chat {chat_id}: {e}")
            return []

__all__ = ["FileService"]
