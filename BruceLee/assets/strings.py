class Strings:
    """User-facing strings"""
    
    # Status messages
    LOADING = "⏳ Please wait..."
    SUCCESS = "✅ Success!"
    ERROR = "❌ Error!"
    WARNING = "⚠️ Warning!"
    
    # Common messages
    WELCOME = "👋 Welcome!"
    GOODBYE = "👋 Goodbye!"
    THANK_YOU = "Thank you!"
    
    # File messages
    FILE_UPLOADED = "📤 File uploaded successfully!"
    FILE_DOWNLOADED = "📥 File downloaded!"
    FILE_DELETED = "🗑️ File deleted!"
    
    # Error messages
    NOT_AUTHORIZED = "❌ You are not authorized!"
    NOT_FOUND = "❌ Not found!"
    ALREADY_EXISTS = "⚠️ Already exists!"
    INVALID_INPUT = "❌ Invalid input!"
    
    # Confirmation
    ARE_YOU_SURE = "🤔 Are you sure?"
    CONFIRM_DELETE = "⚠️ This action cannot be undone. Continue?"
    
    # Pagination
    PAGE = "Page {current}/{total}"
    NO_MORE_RESULTS = "📭 No more results!"

__all__ = ["Strings"]
