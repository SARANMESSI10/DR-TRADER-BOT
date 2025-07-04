import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from modules.menu import get_main_menu
from modules.handlers import handle_option

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name or "BOSS"
    await update.message.reply_text(
        f"Hello {user} 👋\nSARAH is online and ready to confirm trades!",
        reply_markup=get_main_menu()
    )

async def reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    await handle_option(text, update, context)

app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_handler))

if __name__ == "__main__":
    app.run_polling()
