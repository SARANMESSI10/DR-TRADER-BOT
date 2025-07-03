import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread
from strategies.rsi import check_rsi_signal

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get Telegram token from environment variable
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Telegram bot TOKEN is not set in environment variables.")

# Flask server to keep the bot alive (for Render and similar platforms)
app = Flask(__name__)

@app.route('/')
def home():
    return "DR-TRADER-BOT is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Telegram bot command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to DR-TRADER-BOT! Type /trade to get trading advice.")

async def trade(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    signal = await check_rsi_signal()
    await update.message.reply_text(signal)

if __name__ == '__main__':
    # Start Flask server in background
    Thread(target=run_flask).start()

    # Start Telegram bot
    telegram_app = Application.builder().token(TOKEN).build()
    telegram_app.add_handler(CommandHandler("start", start))
    telegram_app.add_handler(CommandHandler("trade", trade))
    telegram_app.run_polling()
