from telethon.tl.types import InlineKeyboardMarkup, InlineKeyboardButton

class Keyboards:
    """Keyboard and button templates"""
    
    @staticmethod
    def file_button(file_id, file_name):
        """Create file share button"""
        return InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text=f"📥 {file_name}",
                callback_data=f"file_{file_id}".encode()
            )
        ]])
    
    @staticmethod
    def search_results(files):
        """Create search results keyboard"""
        buttons = []
        for file in files:
            button = InlineKeyboardButton(
                text=f"📄 {file.file_name}",
                callback_data=f"file_{file.file_id}".encode()
            )
            buttons.append([button])
        return InlineKeyboardMarkup(buttons) if buttons else None
    
    @staticmethod
    def pagination(page, total_pages, prefix="page"):
        """Create pagination keyboard"""
        buttons = []
        
        # Previous button
        if page > 1:
            buttons.append(InlineKeyboardButton(
                text="⬅️ Previous",
                callback_data=f"{prefix}_{page-1}".encode()
            ))
        
        # Page indicator
        buttons.append(InlineKeyboardButton(
            text=f"{page}/{total_pages}",
            callback_data=f"page_info".encode()
        ))
        
        # Next button
        if page < total_pages:
            buttons.append(InlineKeyboardButton(
                text="Next ➡️",
                callback_data=f"{prefix}_{page+1}".encode()
            ))
        
        return InlineKeyboardMarkup([buttons])
    
    @staticmethod
    def confirm_buttons():
        """Create confirmation buttons"""
        return InlineKeyboardMarkup([[
            InlineKeyboardButton(text="✅ Yes", callback_data=b"confirm_yes"),
            InlineKeyboardButton(text="❌ No", callback_data=b"confirm_no")
        ]])

__all__ = ["Keyboards"]
