from telegram_bot import TelegramBot
import os

token = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
bot = TelegramBot(token)
bot.start()
bot.send_message(chat_id=12345, text="Hello King Voldus!")
