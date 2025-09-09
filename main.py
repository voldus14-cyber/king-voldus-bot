from telegram.ext import Updater, CommandHandler
from keep_alive import keep_alive

# Replace with your bot token
BOT_TOKEN = "8128245543:AAFOZIk-NQD8ROABln-JjywZKpqbuWvdVUA"

def start(update, context):
    update.message.reply_text("✅ Bot is alive!")

keep_alive()

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

print("✅ Bot is running and polling...")
updater.start_polling()
updater.idle()
