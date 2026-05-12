"""
BruceLee - Telegram File Sharing Bot
A modern Telethon-based bot for sharing files in Telegram groups
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__license__ = "MIT"

from core import client
from database import init_db
from logger import logger

__all__ = ["client", "init_db", "logger"]
