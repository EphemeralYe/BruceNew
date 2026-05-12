import os
from dotenv import load_dotenv

load_dotenv()

# Telethon Configuration
API_ID = int(os.getenv("API_ID", "15697434"))
API_HASH = os.getenv("API_HASH", "030edfd383cecc96bee1c9a8addccc5d")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7880763749:AAEq8czTTs5YHXppwpFVGR1_rLbxFyD9Xio")

# Database Configuration
DB_URI = os.getenv("DB_URI", "sqlite:///brucelee.db")
DB_NAME = os.getenv("DB_NAME", "brucelee_db")

# Bot Settings
BOT_USERNAME = os.getenv("BOT_USERNAME", "brucelee_bot")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "")
FORCE_SUB_GROUP = os.getenv("FORCE_SUB_GROUP", "")

# File Settings
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 2147483648))  # 2GB in bytes
ALLOWED_FILE_TYPES = os.getenv("ALLOWED_FILE_TYPES", "").split(",")

# Feature Flags
ENABLE_BROADCAST = os.getenv("ENABLE_BROADCAST", "true").lower() == "true"
ENABLE_FORCESUB = os.getenv("ENABLE_FORCESUB", "true").lower() == "true"
ENABLE_INLINE = os.getenv("ENABLE_INLINE", "true").lower() == "true"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
