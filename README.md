# BruceLee - Telegram File Sharing Bot

A modern, scalable Telegram file-sharing bot built with **Telethon**. Share files in groups with button-based sharing to PM.

## Features

✅ **Group File Sharing** - Upload files in groups, create shareable buttons
✅ **PM File Delivery** - Click button → file delivered to user PM
✅ **File Search** - `/search` command to find files
✅ **User Management** - Track users, ban system
✅ **Broadcasting** - Send messages to all users
✅ **Force Subscribe** - Require channel/group subscription
✅ **Admin Commands** - Full admin panel
✅ **Database** - SQLAlchemy ORM with SQLite
✅ **Logging** - Comprehensive logging system
✅ **Modular Architecture** - Clean, scalable code structure

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/brucelee-bot.git
cd BruceLee
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment
```bash
cp .env.example .env
```

### 4. Configure .env
Edit `.env` with your credentials:
```env
API_ID=123456789
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
OWNER_ID=your_user_id
```

Get API_ID and API_HASH from [my.telegram.org](https://my.telegram.org)

### 5. Run Bot
```bash
python -m BruceLee
```

Or:
```bash
python BruceLee/__main__.py
```

## Project Structure

```
BruceLee/
├── core/                 # Bot initialization & decorators
├── database/             # Models and database operations
├── handlers/             # Event handlers for commands/messages
├── services/             # Business logic layer
├── utils/                # Utilities & helpers
├── middlewares/          # Authentication & authorization
├── templates/            # Message & keyboard templates
├── assets/               # Static strings & resources
├── config.py             # Configuration management
├── constants.py          # App-wide constants
├── logger.py             # Logging setup
├── __init__.py           # Package initialization
└── __main__.py           # Entry point
```

## Usage

### User Commands
```
/start    - Start bot
/help     - Show help menu
/search   - Search for files
```

### Admin Commands
```
/stats    - View statistics
/broadcast - Send message to all users
/ban      - Ban a user
```

### Group Usage
1. Upload document in group
2. Bot creates shareable button
3. User clicks button
4. File delivered to PM

## Database Models

- **User** - User information & settings
- **Chat** - Group/channel information  
- **FileMetadata** - File information & metadata
- **FilterIndex** - Search index for files
- **BroadcastLog** - Broadcast history

## Configuration

All settings in `config.py` and `.env`:

| Variable | Description |
|----------|-------------|
| API_ID | Telegram API ID |
| API_HASH | Telegram API Hash |
| BOT_TOKEN | Bot token from @BotFather |
| OWNER_ID | Your user ID |
| DB_URI | Database connection string |
| FORCE_SUB_CHANNEL | Channel to force subscribe |
| MAX_FILE_SIZE | Maximum file size in bytes |

## Development

### Adding New Commands
1. Create handler in `handlers/commands.py`
2. Register in `handlers/__init__.py`

### Adding New Database Models
1. Add model in `database/models.py`
2. Create service methods in `database/`

### Adding Features
1. Create service in `services/`
2. Create handler in `handlers/`
3. Register handler in `handlers/__init__.py`

## License

MIT License - See LICENSE file

## Support

For issues and questions, open an issue or contact support.

---

Made with ❤️ by BruceLee Bot Team
