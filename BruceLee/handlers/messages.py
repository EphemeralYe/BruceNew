from telethon import events
from telethon.tl.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import UserService, FileService, IAFilterService
from constants import CB_FILE_PREFIX
from logger import logger

async def group_message_handler(event):
    """Handle messages in groups"""
    try:
        # Register user
        sender = await event.get_sender()
        UserService.add_user(
            user_id=sender.id,
            username=sender.username,
            first_name=sender.first_name
        )
        
        # Store file metadata if document
        if event.document:
            file_id = event.media.document.id
            file_name = event.document.attributes[0].file_name if hasattr(event.document.attributes[0], 'file_name') else "Unknown"
            
            FileService.add_file(
                file_id=file_id,
                file_name=file_name,
                file_size=event.document.size,
                mime_type=event.document.mime_type,
                uploader_id=sender.id,
                chat_id=event.chat_id
            )
            
            # Add to filter index
            IAFilterService.add_filter(
                chat_id=event.chat_id,
                keyword=file_name.split('.')[0],  # Index by filename
                file_id=file_id,
                file_name=file_name
            )
            
            # Create inline button
            button = InlineKeyboardButton(
                text="📥 Get File",
                callback_data=f"{CB_FILE_PREFIX}{file_id}".encode()
            )
            keyboard = InlineKeyboardMarkup([[button]])
            
            await event.reply(
                f"📄 **{file_name}**\nSize: {format_bytes(event.document.size)}",
                buttons=keyboard
            )
    except Exception as e:
        logger.error(f"Error in group_message_handler: {e}")

async def pm_message_handler(event):
    """Handle PM messages for search and file requests"""
    try:
        sender = await event.get_sender()
        UserService.add_user(
            user_id=sender.id,
            username=sender.username,
            first_name=sender.first_name
        )
        
        message = event.message.text
        
        # Search for files
        if message.startswith("/search "):
            query = message.replace("/search ", "")
            results = FileService.search_files(query, limit=10)
            
            if not results:
                await event.reply("❌ No files found!")
                return
            
            # Create buttons for each file
            buttons = []
            for result in results:
                button = InlineKeyboardButton(
                    text=f"📄 {result.file_name}",
                    callback_data=f"{CB_FILE_PREFIX}{result.file_id}".encode()
                )
                buttons.append([button])
            
            await event.reply("🔍 **Search Results:**", buttons=buttons)
    except Exception as e:
        logger.error(f"Error in pm_message_handler: {e}")

def format_bytes(bytes):
    """Format bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} TB"

async def register_message_handlers(client):
    """Register message handlers"""
    # Group messages
    client.add_event_handler(group_message_handler, events.NewMessage())
    # PM messages
    client.add_event_handler(pm_message_handler, events.NewMessage(private=True))
    logger.info("✅ Message handlers registered")

__all__ = ["register_message_handlers", "group_message_handler", "pm_message_handler", "format_bytes"]
