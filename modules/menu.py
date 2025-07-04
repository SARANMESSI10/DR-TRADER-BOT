from telegram import ReplyKeyboardMarkup

def get_main_menu():
    menu = [
        ["1️⃣ Set Watchlist", "2️⃣ Set Trade Conditions"],
        ["3️⃣ View Watchlist", "4️⃣ View Conditions"],
        ["5️⃣ Start Live Trade Alerts", "6️⃣ Stop Alerts"],
        ["7️⃣ Add Stock Note", "8️⃣ View Stock Notes"],
        ["9️⃣ Show Last Trade Alerts", "🔟 Set Notification Time"],
        ["1️⃣1️⃣ Auto Mode ON/OFF", "1️⃣2️⃣ Add Notes to Stock"],
        ["1️⃣3️⃣ Add New Screener Rule", "1️⃣4️⃣ Export My Settings"],
        ["1️⃣5️⃣ Import Settings", "1️⃣6️⃣ Delete Stock from Watchlist"],
        ["1️⃣7️⃣ Set Custom Screener URL", "1️⃣8️⃣ Backtest Last Week"],
        ["1️⃣9️⃣ Show Top 3 RSI Picks", "2️⃣0️⃣ Enable Email Alerts"],
        ["2️⃣1️⃣ Add to Ignore List", "2️⃣2️⃣ View Ignore List"],
        ["2️⃣3️⃣ Set Alert Sound", "2️⃣4️⃣ Enable Telegram Pin"],
        ["2️⃣5️⃣ Night Mode ON/OFF", "2️⃣6️⃣ Reset All Data"],
        ["2️⃣7️⃣ Trade Summary Report", "2️⃣8️⃣ Market Mood Scanner"],
        ["2️⃣9️⃣ Help / Support", "3️⃣0️⃣ Exit SARAH"],
    ]
    return ReplyKeyboardMarkup(menu, resize_keyboard=True)
