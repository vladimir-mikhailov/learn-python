# Напишите программу, удаляющую из текста все слова,
# в которых присутствуют все буквы "абв".

txt = 'КАвбы, я, бвыла, царицей, – моблвила одна девица.'
letters = 'абв'

translation_map = str.maketrans('.,!-_–:;()', '          ')
txt_lst = [x for x in txt.translate(translation_map).split()]

# Здесь можно описать все варианты знаков препинания, но это долго
for word in txt_lst:
    if set(letters.casefold()).issubset(set(word.casefold())):
        txt = txt \
            .replace(' ' + word, '') \
            .replace(word + ' ', '') \
            .replace(word, '') \
            .replace(',,', ',') \

if txt.startswith((',', '.', '–')):
    txt = txt[1:].lstrip()

txt = txt.capitalize()

print(txt)
