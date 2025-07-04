import json
from telegram import Update
from telegram.ext import CallbackContext
from modules.menu import get_main_menu

DATA_FILE = "sarah_data.json"

# Initialize data file
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"watchlist": [], "conditions": [], "notes": {}, "ignore": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# MAIN HANDLER
def handle_user_input(update: Update, context: CallbackContext):
    text = update.message.text
    chat_id = update.effective_chat.id
    data = load_data()

    if text == "1️⃣ Set Watchlist":
        update.message.reply_text("📈 Send the stock symbols separated by comma (e.g., INFY, TCS, RELIANCE):")
        context.user_data["expecting"] = "watchlist"

    elif text == "2️⃣ Set Trade Conditions":
        update.message.reply_text("📊 Send a condition like: RSI < 30 and P/E < 20")
        context.user_data["expecting"] = "condition"

    elif text == "3️⃣ View Watchlist":
        wl = data["watchlist"]
        msg = "📋 Your Watchlist:\n" + "\n".join(wl) if wl else "❌ Watchlist is empty."
        update.message.reply_text(msg)

    elif text == "4️⃣ View Conditions":
        conds = data["conditions"]
        msg = "📜 Your Conditions:\n" + "\n".join(conds) if conds else "❌ No conditions set."
        update.message.reply_text(msg)

    elif text == "9️⃣ Show Last Trade Alerts":
        update.message.reply_text("🚨 [Sample] Last 5 trade alerts:\n1. INFY - RSI < 30\n2. TCS - PE < 20")

    elif text == "3️⃣0️⃣ Exit SARAH":
        update.message.reply_text("🛑 SARAH is offline now. Type /start to relaunch.")

    else:
        update.message.reply_text("🤖 Choose from the menu below:", reply_markup=get_main_menu())

# SAVE WATCHLIST OR CONDITION
def handle_text_input(update: Update, context: CallbackContext):
    user_input = update.message.text
    data = load_data()

    if context.user_data.get("expecting") == "watchlist":
        symbols = [s.strip().upper() for s in user_input.split(",")]
        data["watchlist"] = list(set(data["watchlist"] + symbols))
        save_data(data)
        update.message.reply_text(f"✅ Watchlist updated:\n" + "\n".join(data["watchlist"]))
    elif context.user_data.get("expecting") == "condition":
        data["conditions"].append(user_input.strip())
        save_data(data)
        update.message.reply_text("✅ Condition saved.")

    context.user_data["expecting"] = None
