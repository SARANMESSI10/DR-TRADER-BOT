import os
from dotenv import load_dotenv
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Flask app for keeping bot alive
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return 'SARAH is alive and monitoring trades!'

# Telegram command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello BOSS! SARAH is online and fully operational.")

# Build the telegram bot application
telegram_app = Application.builder().token(TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))

# Run both Flask and Telegram bot
if __name__ == "__main__":
    import threading

    # Run telegram bot in separate thread
    def run_bot():
        telegram_app.run_polling()

    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Run Flask app (useful for keeping alive on Render)
    flask_app.run(host="0.0.0.0", port=10000)
