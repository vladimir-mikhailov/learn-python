from telegram import Update
from telegram.ext import ContextTypes
from decorators.send_action import send_typing_action
from .help import help_command


@send_typing_action
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Не понимаю такую команду.")
    await help_command(update, context)
