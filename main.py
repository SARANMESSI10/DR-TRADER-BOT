from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os, asyncio

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # e.g. https://your-service-name.onrender.com

flask_app = Flask(__name__)

# 1. Command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, Boss! SARAH is now live.")

# 2. Telegram Application
telegram_app = ApplicationBuilder().token(TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))

# 3. Flask Webhook
@flask_app.route("/webhook", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    await telegram_app.process_update(update)
    return "ok"

# 4. Set Telegram Webhook when Flask boots
@flask_app.before_first_request
def init_webhook():
    async def _set_webhook():
        await telegram_app.bot.set_webhook(WEBHOOK_URL + "/webhook")
    asyncio.get_event_loop().run_until_complete(_set_webhook())

# 5. Run Flask
if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=10000)
