# 🚀 Quick Start Guide

## Prerequisites
- Python 3.8+
- Telegram Account
- Bot Token (from @BotFather)

## Step-by-Step Setup

### 1️⃣ Get Credentials

**API ID & API Hash:**
1. Go to https://my.telegram.org
2. Login with your phone
3. Go to "API development tools"
4. Create an app or use existing one
5. Copy API ID and API Hash

**Bot Token:**
1. Open @BotFather on Telegram
2. Send `/newbot`
3. Follow instructions
4. Copy the token provided

### 2️⃣ Install & Configure

```bash
# Install dependencies
pip install -r requirements.txt

# Copy example env
cp .env.example .env

# Edit .env with your credentials
nano .env
```

Fill in your `.env`:
```env
API_ID=YOUR_API_ID
API_HASH=YOUR_API_HASH
BOT_TOKEN=YOUR_BOT_TOKEN
OWNER_ID=YOUR_USER_ID
```

### 3️⃣ Run Bot

```bash
python -m BruceLee
```

You should see:
```
✅ Bot started as @your_bot_name
✅ Database initialized successfully
✅ Command handlers registered
✅ Message handlers registered
✅ Bot is running!
```

### 4️⃣ Test Bot

1. Open your bot in Telegram (@your_bot_name)
2. Send `/start`
3. Send `/help`
4. Create a group and add your bot
5. Upload a file in the group
6. Click the share button

## Common Issues

### "API ID not found"
- Check you copied API ID correctly from my.telegram.org
- Make sure it's in .env file

### "Bot token invalid"
- Verify token from @BotFather is correct
- Make sure there are no extra spaces

### "Database locked"
- Close other instances of the bot
- Delete *.db-journal files if they exist

### "Module not found"
- Run `pip install -r requirements.txt`
- Make sure you're in the correct directory

## Next Steps

1. **Customize** - Edit message templates in `templates/`
2. **Add Features** - Create new handlers in `handlers/`
3. **Configure** - Adjust settings in `config.py`
4. **Deploy** - Use your hosting provider

## File Structure Overview

```
BruceLee/
├── core/              → Bot setup & decorators
├── database/          → Data models & queries
├── handlers/          → Event handlers
├── services/          → Business logic
├── utils/             → Helper functions
├── templates/         → Messages & keyboards
├── config.py          → Configuration
├── __main__.py        → Start here!
└── requirements.txt   → Dependencies
```

## Useful Commands

**Development:**
```bash
# Run with logging
python -m BruceLee

# Install dev dependencies
pip install -r requirements.txt

# Check Python version
python --version
```

**Database:**
```bash
# Reset database
rm brucelee.db
python -m BruceLee
```

## Documentation

- **Telethon Docs**: https://docs.telethon.dev
- **Telegram Bot API**: https://core.telegram.org/bots/api
- **SQLAlchemy**: https://docs.sqlalchemy.org

## Support

- 📖 Read README.md
- 🐛 Check GitHub Issues
- 💬 Ask in Telegram groups
- 📧 Email support@example.com

---

🎉 **You're ready!** Happy coding!
