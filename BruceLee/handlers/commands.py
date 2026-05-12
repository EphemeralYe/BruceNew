from telethon import events
from core import owner_only
from database import UserService
from constants import MSG_START, MSG_HELP
from logger import logger

async def start_handler(event):
    """Handle /start command"""
    try:
        sender = await event.get_sender()
        UserService.add_user(
            user_id=sender.id,
            username=sender.username,
            first_name=sender.first_name,
            last_name=sender.last_name
        )
        await event.reply(MSG_START)
    except Exception as e:
        logger.error(f"Error in start_handler: {e}")
        await event.reply("❌ An error occurred!")

async def help_handler(event):
    """Handle /help command"""
    try:
        await event.reply(MSG_HELP)
    except Exception as e:
        logger.error(f"Error in help_handler: {e}")

@owner_only
async def stats_handler(event):
    """Handle /stats command - Owner only"""
    try:
        user_count = UserService.get_user_count()
        await event.reply(f"""
📊 **Bot Statistics**
👥 Total Users: {user_count}
        """)
    except Exception as e:
        logger.error(f"Error in stats_handler: {e}")
        await event.reply("❌ An error occurred!")

async def register_command_handlers(client):
    """Register all command handlers"""
    client.add_event_handler(start_handler, events.NewMessage(pattern="/start"))
    client.add_event_handler(help_handler, events.NewMessage(pattern="/help"))
    client.add_event_handler(stats_handler, events.NewMessage(pattern="/stats"))
    logger.info("✅ Command handlers registered")

__all__ = ["register_command_handlers", "start_handler", "help_handler", "stats_handler"]
