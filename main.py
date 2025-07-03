# main.py

import threading
import os
import requests
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# === LOAD ENVIRONMENT VARIABLES ===
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# === TELEGRAM BOT SETUP ===
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
    flask_app.run(host='0.0.0.0', port=10000)

# === RUN BOTH TOGETHER ===
if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    run_flask()
