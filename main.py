from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from modules.menu import get_main_menu
from modules.handlers import handle_user_input, handle_text_input

TOKEN = "YOUR_BOT_TOKEN"  # Replace with your actual token

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello BOSS! SARAH is online and ready to confirm trades.",
        reply_markup=get_main_menu()
    )

# main()
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_router))

    print("SARAH is running...")
    app.run_polling()

# router for handling input
async def handle_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "expecting" in context.user_data and context.user_data["expecting"]:
        handle_text_input(update, context)
    else:
        handle_user_input(update, context)

if __name__ == "__main__":
    main()
