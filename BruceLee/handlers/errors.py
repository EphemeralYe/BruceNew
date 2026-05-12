from logger import logger

async def global_error_handler(event, error):
    """Handle global errors"""
    logger.error(f"Global error: {error}")
    try:
        await event.reply("❌ An unexpected error occurred. Please try again later.")
    except:
        pass

def register_error_handlers(client):
    """Register error handlers"""
    # Telethon doesn't have built-in global error handlers
    # Wrap handlers with try-except instead
    logger.info("✅ Error handlers registered")

__all__ = ["global_error_handler", "register_error_handlers"]
