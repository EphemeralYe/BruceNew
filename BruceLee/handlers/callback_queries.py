from telethon import events
from telethon.tl.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import FileService
from constants import CB_FILE_PREFIX
from logger import logger

async def handle_file_button(event):
    """Handle file button clicks from inline queries"""
    try:
        callback_data = event.data.decode('utf-8')
        
        if callback_data.startswith(CB_FILE_PREFIX):
            file_id = callback_data.replace(CB_FILE_PREFIX, '')
            
            # Get file metadata
            file_meta = FileService.get_file(file_id)
            
            if not file_meta:
                await event.answer("❌ File not found!", alert=True)
                return
            
            # Send file to user's PM
            await event.client.send_file(
                event.sender_id,
                file_meta.file_id,
                caption=f"📄 **{file_meta.file_name}**\nSize: {format_bytes(file_meta.file_size)}"
            )
            
            await event.answer("✅ File sent to your PM!", alert=True)
    except Exception as e:
        logger.error(f"Error in handle_file_button: {e}")
        await event.answer("❌ An error occurred!", alert=True)

def format_bytes(bytes):
    """Format bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} TB"

async def register_callback_handlers(client):
    """Register callback query handlers"""
    client.add_event_handler(handle_file_button, events.CallbackQuery())
    logger.info("✅ Callback handlers registered")

__all__ = ["register_callback_handlers", "handle_file_button", "format_bytes"]
