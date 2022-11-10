# Напишите программу, удаляющую из текста все слова,
# в которых присутствуют все буквы "абв".

txt = 'КАвбы я бвыла царицей, – моблвила одна девица.'
letters = 'абв'

translation_map = str.maketrans('.,!-_–:;()', '          ')
for word in [x for x in txt.translate(translation_map).split()]:
    if set(letters.casefold()).issubset(set(word.casefold())):
        txt = txt.replace(word, '').replace('  ', ' ').strip()

if txt.startswith((',', '.', '–')):
    txt = txt[1:].lstrip()

txt = txt.capitalize()

print(txt)
