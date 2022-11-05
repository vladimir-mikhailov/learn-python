# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('1.txt', 'r', encoding='utf-8') as file:
    lst = [int(i) for i in file.read().split()]

print(lst)

for i in range(len(lst) - 1):
    if lst[i + 1] - lst[i] != 1:
        print('Не хватает:', lst[i] + 1)
