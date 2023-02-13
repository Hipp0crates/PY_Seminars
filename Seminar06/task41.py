# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов, у которых оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве.
# Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

from random import randint


def amount_elements(sp, j=0):
    for i in range(1, len(sp)-1):
        if sp[i-1] < sp[i] and sp[i] > sp[i+1]:
            j += 1
    print(f'Количество элементов: {j}')


n = int(input('Введите длинну массива: '))

for i in range(4):
    lst1 = [randint(1, 9) for _ in range(n)]
    print(f'Прогон {i+1}')
    print(lst1)
    amount_elements(lst1)
    print()