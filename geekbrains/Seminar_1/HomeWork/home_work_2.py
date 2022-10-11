# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from itertools import product

# Вариант без itertools
print(all((not (x or y or z) == (not x and not y and not z))
          for z in [0, 1] for y in [0, 1] for x in [0, 1]))

# Вариант с itertools
print(all((not (x or y or z) == (not x and not y and not z))
      for x, y, z in product(*((True, False),) * 3, )))
