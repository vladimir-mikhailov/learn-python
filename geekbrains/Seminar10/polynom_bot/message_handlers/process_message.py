from telegram import Update
from telegram.ext import ContextTypes

import utils.polynom as p


async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Принимаем многочлен."""
    message = update.message.text
    try:
        if '\n' in message:
            strings = message.split('\n')
        polynomes = [p.get_coefficients(m) for m in strings]
        reply_text = '\n+\n'.join(strings)
        reply_text += '\n=\n'
        reply_text += p.get_polynome(p.sum_polynomes(polynomes))

    except Exception as e:
        reply_text = 'Это не список многочленов с новой строки.'
        # print('Ошибка: ', e)

    await update.message.reply_text(reply_text)
