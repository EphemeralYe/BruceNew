from .commands import register_command_handlers
from .callback_queries import register_callback_handlers
from .messages import register_message_handlers
from .inline_queries import register_inline_handlers
from .errors import register_error_handlers

async def register_all_handlers(client):
    """Register all handlers"""
    await register_command_handlers(client)
    await register_callback_handlers(client)
    await register_message_handlers(client)
    await register_inline_handlers(client)
    register_error_handlers(client)

__all__ = [
    "register_all_handlers",
    "register_command_handlers",
    "register_callback_handlers",
    "register_message_handlers",
    "register_inline_handlers",
    "register_error_handlers"
]
