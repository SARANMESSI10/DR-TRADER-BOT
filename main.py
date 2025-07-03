from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os, asyncio

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # e.g., https://your-render.onrender.com

flask_app = Flask(__name__)

# 1. Telegram command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, Boss! SARAH is now active.")

# 2. Telegram application setup
telegram_app = ApplicationBuilder().token(TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))

# 3. Flask webhook
@flask_app.route("/webhook", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    await telegram_app.process_update(update)
    return "OK"

# 4. Set webhook
@flask_app.before_first_request
def set_webhook():
    async def _set():
        await telegram_app.bot.set_webhook(WEBHOOK_URL + "/webhook")
    asyncio.get_event_loop().run_until_complete(_set())

# 5. Run
if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=10000)
