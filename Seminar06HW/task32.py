# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


def index_values(array, min_value, max_value):
    sp = []
    for i in range(len(array)):
        if min_value <= array[i] and array[i] <= max_value:
            sp.append(i)
    print(
        f'Индексы элементов в диапозоне значений от {min_value} до {max_value}:\n{sp}')


try:
    while True:
        n = int(input('Введите количество элементов списка: '))
        lst = [randint(-10, 10) for _ in range(n)]
        print(lst)
        min = int(input('Введите минимальное значение: '))
        max = int(input('Введите максимальное значение: '))
        index_values(lst, min, max)
        print()
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
