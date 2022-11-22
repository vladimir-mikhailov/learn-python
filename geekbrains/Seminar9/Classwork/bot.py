from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from task1 import change


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    txt = update.message.text

    letters = 'абв'

    words_only = [x for x in txt.translate(
        str.maketrans('.,!-_–:;()', '          ')).split()]

    for word in words_only:
        if set(letters.casefold()).issubset(set(word.casefold())):
            txt = txt.replace(word, '').replace('  ', ' ').strip()

    if txt.startswith((',', '.', '–')):
        txt = txt[1:].lstrip()

    await update.message.reply_text(txt.capitalize())


app = ApplicationBuilder().token(
    "5841890239:AAH2k52U3kWDYA6a51kdorZ1F1gNr9lz7Ks").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()

# /hello абв фывафыва фыва
