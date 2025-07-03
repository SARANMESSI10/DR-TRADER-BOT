import os
from flask import Flask
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Flask app for Render health check
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

# Telegram command handler
async def start(update, context):
    await update.message.reply_text("Hello, I am your trading bot! 🚀")

# Start Telegram bot
def start_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    import threading
    threading.Thread(target=start_bot).start()
    flask_app.run(host="0.0.0.0", port=8080)
