from flask import Flask
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

# --- Setup Flask ---
app = Flask(__name__)

@app.route('/')
def index():
    return 'King Voldus Bot is running.'

# --- Telegram Bot Setup ---
TOKEN = os.environ.get("8128245543:AAFOZIk-NQD8ROABln-JjywZKpqbuWvdVUA")
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

def start(update, context):
    update.message.reply_text('Voldus bot activated.')

dispatcher.add_handler(CommandHandler("start", start))

# --- Polling (Alternative to webhook) ---
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
