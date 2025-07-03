import os
from flask import Flask
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
from strategies.rsi import check_rsi_signal

# Load .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running with RSI strategy!"

# /start command
async def start(update, context):
    await update.message.reply_text("Welcome to DR TRADER BOT 🧠📈\nUse /rsi to get RSI signal.")

# /rsi command
async def rsi(update, context):
    symbol = context.args[0] if context.args else "BTC-USD"
    try:
        signal = check_rsi_signal(symbol)
        await update.message.reply_text(signal)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

# Start bot + Flask
def start_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rsi", rsi))
    app.run_polling()

if __name__ == "__main__":
    import threading
    threading.Thread(target=start_bot).start()
    flask_app.run(host="0.0.0.0", port=8080)
