from flask import Flask, request
import telegram
import os

# Set up Flask app
app = Flask(__name__)

# Read bot token from environment variable
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=BOT_TOKEN)

# Your strategy logic (example: RSI)
from strategies.rsi import should_buy, should_sell

@app.route("/", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text.lower()

    # Basic commands
    if "buy" in text and should_buy():
        bot.send_message(chat_id=chat_id, text="✅ Buy Signal Triggered!")
    elif "sell" in text and should_sell():
        bot.send_message(chat_id=chat_id, text="❌ Sell Signal Triggered!")
    else:
        bot.send_message(chat_id=chat_id, text="⚠️ No action or unrecognized command.")

    return "ok"

@app.route("/", methods=["GET", "HEAD"])
def index():
    return "SARAH Trading Bot is live."

# 👇 Required for Render (uses production WSGI server)
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
