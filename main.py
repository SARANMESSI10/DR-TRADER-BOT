from flask import Flask, request
import telegram
import os

# Set up Flask app
app = Flask(__name__)

# Bot token
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=BOT_TOKEN)

# Strategy logic (mock for now)
print("Skipping RSI import for testing")


@app.route("/", methods=["POST"])
def webhook():
    try:
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        if update.message:
            chat_id = update.message.chat.id
            text = update.message.text.lower()

            if text == "/start":
                bot.send_message(chat_id=chat_id, text="👋 Hello BOSS! SARAH is online and ready to confirm trades.")
            elif "buy" in text and should_buy():
                bot.send_message(chat_id=chat_id, text="✅ Buy Signal Triggered!")
            elif "sell" in text and should_sell():
                bot.send_message(chat_id=chat_id, text="❌ Sell Signal Triggered!")
            else:
                bot.send_message(chat_id=chat_id, text="⚠️ No trade signal or unknown command.")

    except Exception as e:
        print(f"Error: {e}")

    return "ok", 200

@app.route("/", methods=["GET", "HEAD"])
def index():
    return "SARAH Trading Bot is live."

# Production server setup for Render
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
