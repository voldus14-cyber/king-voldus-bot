from bot_base import BaseBot

class TelegramBot(BaseBot):
    def send_message(self, chat_id, text):
        print(f"Sending to {chat_id}: {text}")
