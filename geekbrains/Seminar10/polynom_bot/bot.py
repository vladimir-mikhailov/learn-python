import os
import logging

from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes

from command_handlers.start import start
from command_handlers.help import help_command
from command_handlers.unknown import unknown
from message_handlers.process_message import process_message

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler(['start', 'restart'], start))
    app.add_handler(CommandHandler(['help'], help_command))
    app.add_handler(MessageHandler(
        filters.TEXT & (~filters.COMMAND), process_message))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    app.run_polling()


# Commands for BotFather:
# help - Показать, что я умею.
