#!/usr/bin/env python3
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token - you'll need to get this from @BotFather on Telegram
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am your Telegram bot. How can I help you?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
Available commands:
/start - Start the bot
/help - Show this help message
    """
    await update.message.reply_text(help_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(f"You said: {update.message.text}")

def main() -> None:
    """Start the bot."""
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("Please set your BOT_TOKEN first!")
        print("Get your token from @BotFather on Telegram")
        return

    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Register message handler for text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    print("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()