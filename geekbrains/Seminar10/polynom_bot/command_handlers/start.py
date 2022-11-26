from telegram import Update, ForceReply
from telegram.ext import ContextTypes
from decorators.send_action import send_typing_action
from .help import help_command


@send_typing_action
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет, {user.full_name}!",
        reply_markup=ForceReply(selective=True),
    )
    await help_command(update, context)
