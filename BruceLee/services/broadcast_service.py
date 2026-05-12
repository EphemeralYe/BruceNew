from database import UserService, BroadcastLog
from logger import logger
import uuid
from datetime import datetime

class BroadcastManager:
    """Manage broadcast messages to all users"""
    
    @staticmethod
    async def broadcast_message(client, message_text, broadcast_id=None):
        """Send message to all users"""
        if not broadcast_id:
            broadcast_id = str(uuid.uuid4())
        
        try:
            users = UserService.get_all_users()
            sent_count = 0
            failed_count = 0
            
            for user in users:
                try:
                    if not user.is_banned:
                        await client.send_message(user.user_id, message_text)
                        sent_count += 1
                except Exception as e:
                    logger.error(f"Failed to send to {user.user_id}: {e}")
                    failed_count += 1
            
            # Log broadcast
            BroadcastLog.add_broadcast(
                broadcast_id=broadcast_id,
                message=message_text,
                sent_to=sent_count,
                failed=failed_count
            )
            
            logger.info(f"Broadcast {broadcast_id}: Sent to {sent_count}, Failed {failed_count}")
            return {"sent": sent_count, "failed": failed_count}
        except Exception as e:
            logger.error(f"Broadcast error: {e}")
            return {"sent": 0, "failed": len(UserService.get_all_users())}

__all__ = ["BroadcastManager"]
