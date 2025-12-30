import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Логування в консолі
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm a simple bot. Use /menu to see what I can do.")

# Команда /menu
async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Here are my commands:\n"
        "/whisper [text] — make text whisper (lowercase)\n"
        "/scream [text] — make text scream (uppercase)\n"
        "/menu — show this message"
    )
    await update.message.reply_text(text)

# Команда /whisper
async def whisper_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = " ".join(context.args)
    if not user_text:
        await update.message.reply_text("Example: /whisper HELLO WORLD")
        return
    await update.message.reply_text(user_text.lower())

# Команда /scream
async def scream_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = " ".join(context.args)
    if not user_text:
        await update.message.reply_text("Example: /scream hello world")
        return
    await update.message.reply_text(user_text.upper())

if __name__ == '__main__':
    TOKEN = 'personal_tg_bot_token'

    # Створення додатку
    app = Application.builder().token(TOKEN).build()

    # Опрацювання команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu_command))
    app.add_handler(CommandHandler("whisper", whisper_command))
    app.add_handler(CommandHandler("scream", scream_command))

    print("Bot is running...")
    app.run_polling()