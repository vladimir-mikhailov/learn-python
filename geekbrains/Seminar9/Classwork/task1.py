# Напишите программу, удаляющую из текста все слова,
# в которых присутствуют все буквы "абв".

txt = 'КАвбы я бвыла царицей, – моблвила одна девица.'


def change(txt):

    letters = 'абв'

    words_only = [x for x in txt.translate(
        str.maketrans('.,!-_–:;()', '          ')).split()]

    for word in words_only:
        if set(letters.casefold()).issubset(set(word.casefold())):
            txt = txt.replace(word, '').replace('  ', ' ').strip()

    if txt.startswith((',', '.', '–')):
        txt = txt[1:].lstrip()

    return txt.capitalize()
