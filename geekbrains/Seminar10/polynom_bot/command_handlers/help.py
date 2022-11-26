from telegram import Update, constants
from telegram.ext import ContextTypes
from decorators.send_action import send_typing_action


@send_typing_action
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = '''Вот список команд, которые я знаю:

    /help - Показать, что я умею

    <b>Сложение многочленов:</b>
    Присылайте многочлены в одном сообщении, каждый с новой строки (Shift+Enter).
    А я пришлю результат их сложения.

    Формат многочлена:
    9x^5 + 7x^4 + 7x^3 + 9x^2 + 6x + 17 = 0
    или
    9x^5 + 7x^4 + 7x^3 + 9x^2 + 6x + 17
    '''
    await update.message.reply_text(text=answer, parse_mode=constants.ParseMode.HTML)
