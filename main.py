# main.py

import threading
import requests
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === TELEGRAM BOT SETUP ===
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Replace with your real token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("SARAH is online, BOSS.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

def run_bot():
    app.run_polling()

# === FLASK SERVER ===
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return 'SARAH is awake.'

def run_flask():
    flask_app.run(host='0.0.0.0', port=10000)  # Required for Render

# === RUN BOTH TOGETHER ===
if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    run_flask()
