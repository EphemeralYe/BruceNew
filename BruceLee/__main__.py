#!/usr/bin/env python3
"""
BruceLee Bot - Main Entry Point
"""

import asyncio
import signal
import sys
from logger import logger
from core import client, init_bot, close_bot
from database import init_db
from handlers import register_all_handlers


async def main():
    """Main bot function"""
    try:
        # Initialize database
        logger.info("🔧 Initializing database...")
        await init_db()
        
        # Initialize bot
        logger.info("🤖 Initializing bot...")
        await init_bot()
        
        # Register handlers
        logger.info("📝 Registering handlers...")
        await register_all_handlers(client)
        
        logger.info("✅ Bot is running! Press Ctrl+C to stop.")
        
        # Keep bot running
        await client.run_until_disconnected()
        
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        raise
    finally:
        await close_bot()


def handle_exit_signal(signum, frame):
    """Handle exit signals gracefully"""
    logger.info("⏹️ Shutting down...")
    sys.exit(0)


if __name__ == "__main__":
    # Handle exit signals
    signal.signal(signal.SIGINT, handle_exit_signal)
    signal.signal(signal.SIGTERM, handle_exit_signal)
    
    try:
        # Run the bot
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("⏹️ Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        sys.exit(1)
