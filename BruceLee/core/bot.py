from telethon import TelegramClient
from telethon.sessions import StringSession
from config import API_ID, API_HASH, BOT_TOKEN
from logger import logger
import os

# Initialize Telethon client
session_string = os.getenv("SESSION_STRING", None)

if session_string:
    client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
else:
    client = TelegramClient("brucelee_session", API_ID, API_HASH)

async def init_bot():
    """Initialize the bot and connect to Telegram"""
    try:
        await client.start(bot_token=BOT_TOKEN)
        me = await client.get_me()
        logger.info(f"✅ Bot started as @{me.username}")
        return client
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")
        raise

async def close_bot():
    """Gracefully close bot connection"""
    try:
        await client.disconnect()
        logger.info("✅ Bot disconnected")
    except Exception as e:
        logger.error(f"❌ Error closing bot: {e}")

__all__ = ["client", "init_bot", "close_bot"]
