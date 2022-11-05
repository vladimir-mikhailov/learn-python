# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.

# Пример:

#  [1, 5, 2, 3, 4, 6, 1, 7] = > [1, 2, 3] или[1, 7] или[1, 6, 7] и т.д.

lst = [1, 5, 2, 3, 4, 6, 1, 7]

temp_lst = lst.copy()
sequences = []

for d in range(len(lst) - 1):
    current = temp_lst[0]
    tmp = [current]
    for i in range(1, len(temp_lst)):
        if temp_lst[i] > current:
            tmp.append(temp_lst[i])
            current = temp_lst[i]
            sequences.append(' '.join(map(str, tmp)))

    temp_lst.pop(0)

print(sequences)
