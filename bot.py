import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Help", "About"], ["Website", "Contact"]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Welcome! I'm your bot.\nChoose an option below:",
        reply_markup=markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 *Available Commands:*\n"
        "/start — Show main menu\n"
        "/help — Show this help\n"
        "/about — About this bot\n"
        "/echo — Repeat your message",
        parse_mode="Markdown"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Built with Python, hosted on Railway!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = " ".join(context.args)
    if user_text:
        await update.message.reply_text(f"🔁 {user_text}")
    else:
        await update.message.reply_text("Usage: /echo Hello World")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    responses = {
        "help": "Type /help to see all commands.",
        "about": "Type /about to learn more.",
        "website": "🌐 https://example.com",
        "contact": "📧 hello@example.com",
        "hello": "👋 Hey there!",
        "hi": "👋 Hi! How can I help?",
    }
    reply = responses.get(text, "I don't understand that. Try /help")
    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    print("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
