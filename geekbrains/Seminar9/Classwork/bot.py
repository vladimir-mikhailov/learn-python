import os
import logging

from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from change import change

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, " + str(update.effective_user.first_name))
    await update.message.reply_text("Your Telegram ID is " + str(update.effective_user.id))
    user_says = " ".join(context.args)
    if user_says:
        await update.message.reply_text("You said: " + user_says)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    who_replies = 'Uncle Khryusha-Povtoryusha'
    reply = f'{who_replies}: {update.message.text}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


async def filter_string(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(change(update.message.text))


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler(['start', 'restart'], start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    app.add_handler(CommandHandler('filter', filter_string))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    app.run_polling()
