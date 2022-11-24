from typing import Union, List
from functools import wraps
import os
import logging

from telegram import Update, constants
from telegram.ext import filters, ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes

import calc

if __name__ == '__main__':
    TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
    app = ApplicationBuilder().token(TOKEN).build()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Decorators:

def command_handler(command):
    def decorator(func):
        handler = CommandHandler(command, func)
        app.add_handler(handler)
        return func
    return decorator


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        async def command_func(update, context, *args, **kwargs):
            await context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return await func(update, context,  *args, **kwargs)
        return command_func

    return decorator


send_typing_action = send_action(constants.ChatAction.TYPING)


# Commands:

@send_typing_action
@command_handler(['start'])
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hello_text = "Привет, " + str(update.effective_user.first_name) + '! '
    await context.bot.send_message(chat_id=update.effective_chat.id, text=hello_text)
    await help(update, context)


@send_typing_action
@command_handler('help')
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = '''Вот список команд, которые я знаю:

    /help - Показать, что я умею

    <b>Калькулятор:</b>
    Просто напишите выражение в сообщение, а я пришлю результат.
    '''
    await update.message.reply_text(text=answer, parse_mode=constants.ParseMode.HTML)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = round(calc.solve(update.message.text)[0], 2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


@send_typing_action
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Не понимаю такую команду.")

if __name__ == '__main__':
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))
    app.run_polling()


# Commands for BotFather:
# help - Показать, что я умею
