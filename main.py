from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Bot command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("King Voldus Bot is now active.")

# Entry point
if __name__ == '__main__':
    TOKEN = os.environ.get("BOT_TOKEN")
    
    if not TOKEN:
        raise Exception("BOT_TOKEN not found in environment variables")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()
