from functools import wraps
from config import OWNER_ID
from logger import logger

def owner_only(func):
    """Decorator to restrict command to owner only"""
    @wraps(func)
    async def wrapper(event):
        if event.sender_id != OWNER_ID:
            await event.reply("❌ You don't have permission to use this command.")
            logger.warning(f"Unauthorized access attempt by {event.sender_id}")
            return
        return await func(event)
    return wrapper

def admin_only(func):
    """Decorator to restrict command to admins"""
    @wraps(func)
    async def wrapper(event):
        # You can expand this to check against a list of admin IDs from database
        if event.sender_id != OWNER_ID:
            await event.reply("❌ Admin access required.")
            return
        return await func(event)
    return wrapper

def pm_only(func):
    """Decorator to restrict command to PM only"""
    @wraps(func)
    async def wrapper(event):
        if event.is_private is False:
            await event.reply("⚠️ This command only works in PM.")
            return
        return await func(event)
    return wrapper

def group_only(func):
    """Decorator to restrict command to groups only"""
    @wraps(func)
    async def wrapper(event):
        if event.is_private is True:
            await event.reply("⚠️ This command only works in groups.")
            return
        return await func(event)
    return wrapper

__all__ = ["owner_only", "admin_only", "pm_only", "group_only"]
