from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "✅ Bot is alive and running."

def run():
    app.run(host='0.0.0.0', port=8080)  # ✅ Back to port 8080
    # DO NOT change to 5000 again unless you’re on a paid plan

def keep_alive():
    t = Thread(target=run)
    t.start()
