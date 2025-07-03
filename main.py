import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # e.g. https://your-app.onrender.com

# Flask server
flask_app = Flask(__name__)

# Telegram command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello BOSS 👑 — SARAH is online via Render!")

# Create Telegram bot application
telegram_app = Application.builder().token(TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))

# Webhook endpoint
@flask_app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return "ok", 200

# Set webhook before first request
@flask_app.before_first_request
def setup_webhook():
    asyncio.run(
        telegram_app.bot.set_webhook(WEBHOOK_URL + "/webhook")
    )

# Run Flask server
if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=10000)

