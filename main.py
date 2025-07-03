import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define your handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello BOSS! SARAH RSI bot is online. Send /check to get RSI signal.")

async def check_rsi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from strategies.rsi import check_rsi_signal
    result = check_rsi_signal("AAPL")  # You can change symbol or parse from user input
    await update.message.reply_text(result)

# Start the bot using polling (no Updater)
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check", check_rsi))
    app.run_polling()
