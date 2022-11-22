from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from change import change


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(change(update.message.text))

app = ApplicationBuilder().token(
    "Your_Token here").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()

# /hello абв фывафыва фыва

# https://t.me/vladimir_superbot

# This installs the pre-release of v20

# pip install python-telegram-bot --pre
# python bot.py

# https://t.me/BotFather
