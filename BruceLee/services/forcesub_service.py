from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from logger import logger

class ForceSubManager:
    """Manage force subscription checks"""
    
    @staticmethod
    async def check_subscription(client, user_id):
        """Check if user is subscribed to required channels"""
        if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
            return True  # Force sub disabled
        
        try:
            # Check channel subscription
            if FORCE_SUB_CHANNEL:
                try:
                    await client.get_permissions(FORCE_SUB_CHANNEL, user_id)
                except:
                    return False
            
            # Check group subscription
            if FORCE_SUB_GROUP:
                try:
                    await client.get_permissions(FORCE_SUB_GROUP, user_id)
                except:
                    return False
            
            return True
        except Exception as e:
            logger.error(f"Error checking subscription: {e}")
            return False
    
    @staticmethod
    async def send_forcesub_message(event):
        """Send force subscription message"""
        message = """
⚠️ **Force Subscribe Required**

Please join our channel and group to use this bot:

🔗 Join Channel: {FORCE_SUB_CHANNEL}
🔗 Join Group: {FORCE_SUB_GROUP}

After joining, try again!
        """
        await event.reply(message)

__all__ = ["ForceSubManager"]
