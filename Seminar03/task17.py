# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

from random import randint

n = int(input('Введите количество элементов списка: '))
lst = [randint(-10, 10) for _ in range(n)]
print(lst)

lst = set(lst)
print(lst)
print(f'Количество различных чисел: {len(lst)}')
