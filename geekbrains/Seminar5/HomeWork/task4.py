# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from pathlib import Path


def encode(source_filename, target_filename):
    with open(source_filename, 'r', encoding='utf-8') as file:
        s = file.read()
    encoded = ''
    count = 1
    for i in range(1, len(s)):
        if str(s[i]) == str(s[i-1]):
            count += 1
        else:
            if count > 1:
                encoded += str(count) + str(s[i-1])
            else:
                encoded += str(s[i-1])
            # FIXME: Никаких других символов, кроме тех что присутствуют в строке, в зашифрованной строке быть не должно
            if encoded[-1].isdigit():
                encoded += '▹'
            count = 1
    encoded += str(count) + str(s[i])

    with open(target_filename, 'w', encoding='utf-8') as f:
        f.write(encoded)


def decode(source_filename, target_filename):
    with open(source_filename, 'r', encoding='utf-8') as file:
        encoded = file.read()
    chunks = [s[::-1] for s in list(reversed(encoded.split('▹')))]
    decoded = ''
    for chunk in chunks:
        while len(chunk):
            sym = chunk[0]
            quantity = 1
            if len(chunk) == 1:
                decoded += str(sym)
                break
            if chunk[1:].isdigit():
                quantity = int(chunk[1:][::-1])
                decoded += quantity * str(sym)
                break
            for s in chunk[1:]:
                next_sym_index = 0
                if not s.isdigit():
                    if chunk.find(s) == 1:
                        next_sym_index = 1
                        break
                    else:
                        next_sym_index = chunk[1:].find(s) + 1
                        quantity = int(chunk[1:next_sym_index][::-1])
                        break
            decoded += quantity * sym
            chunk = chunk[next_sym_index:]
    decoded = decoded[::-1]
    with open(target_filename, 'w', encoding='utf-8') as file:
        file.write(decoded)


encode('text_source.txt', 'text_encoded.txt')
decode('text_encoded.txt', 'text_decoded.txt')

source_file_size = Path('text_source.txt').stat().st_size
encoded_file_size = Path('text_encoded.txt').stat().st_size
print('Размер исходного файла:', source_file_size, 'байт')
print('Размер сжатого файла:', encoded_file_size, 'байт')
print(
    f'Эффективность сжатия: {int(encoded_file_size / source_file_size * 100)}%')
