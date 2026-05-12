from database import FileService as FileDB, IAFilterService
from logger import logger

class FileManager:
    """File management business logic"""
    
    @staticmethod
    async def process_uploaded_file(file_id, file_name, file_size, mime_type, uploader_id, chat_id):
        """Process uploaded file"""
        try:
            # Add to database
            success = FileDB.add_file(
                file_id=file_id,
                file_name=file_name,
                file_size=file_size,
                mime_type=mime_type,
                uploader_id=uploader_id,
                chat_id=chat_id
            )
            
            if success:
                # Index for search
                keywords = file_name.split('.')
                for keyword in keywords:
                    IAFilterService.add_filter(
                        chat_id=chat_id,
                        keyword=keyword,
                        file_id=file_id,
                        file_name=file_name
                    )
                logger.info(f"File indexed: {file_name}")
            
            return success
        except Exception as e:
            logger.error(f"Error processing file: {e}")
            return False
    
    @staticmethod
    def search_files(query, limit=10):
        """Search for files"""
        return FileDB.search_files(query, limit)
    
    @staticmethod
    def get_file_details(file_id):
        """Get file details"""
        return FileDB.get_file(file_id)

__all__ = ["FileManager"]
