class Messages:
    """Message templates"""
    
    START = """
👋 **Welcome to BruceLee File Sharing Bot!**

I help you share files easily in groups. Just upload files in a group and I'll create shareable buttons.

**How it works:**
1️⃣ Upload files in a group
2️⃣ Click the share button
3️⃣ File is sent to your PM

**Commands:**
/start - Start the bot
/help - Show help menu
/search <keyword> - Search for files
/stats - Show statistics (Owner only)

📝 Made with ❤️
    """
    
    HELP = """
📚 **Help Menu**

**For Users:**
/start - Start bot
/help - Show this menu
/search <keyword> - Search files in your chat

**For Admin:**
/broadcast <message> - Send message to all users
/stats - View bot statistics
/ban <user_id> - Ban a user

**For Groups:**
Just upload a document and I'll create a share button!

Need help? Contact @Support
    """
    
    FILE_SHARED = "✅ **File Shared!**\n\nClick the button below to receive the file in your PM."
    
    FILE_NOT_FOUND = "❌ **File not found!**\n\nThe file you're looking for doesn't exist."
    
    SEARCH_RESULTS = "🔍 **Search Results**\n\nFound {count} file(s). Select one below:"
    
    SEARCH_NO_RESULTS = "❌ No files found for: `{query}`"
    
    FORCE_SUB = """
⚠️ **Force Subscribe Required**

To use this bot, please subscribe to:

🔗 Join Channel
🔗 Join Group

After joining, try again!
    """
    
    UNAUTHORIZED = "❌ You don't have permission to use this command!"
    
    ERROR = "❌ An error occurred! Please try again later."

__all__ = ["Messages"]
