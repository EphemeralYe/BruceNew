import logging
import sys
from config import LOG_LEVEL

# Create logger
logger = logging.getLogger("BruceLee")
logger.setLevel(getattr(logging, LOG_LEVEL))

# Create handlers
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(getattr(logging, LOG_LEVEL))

# Create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Add formatter to handler
console_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(console_handler)

__all__ = ["logger"]
