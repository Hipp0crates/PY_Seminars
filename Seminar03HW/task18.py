# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.

from random import randint
try:
    N = int(input('Введите количество элементов: '))
    lst = [randint(1, 9) for _ in range(N)]
    sorted_lst = list(set(lst))
    while True:
        print(f'Задан массив: {lst}')
        X = int(input('Введите число: '))

        nearest1 = sorted_lst[0]
        nearest2 = sorted_lst[-1]

        for i in sorted_lst:
            if abs(i - X) < abs(nearest1 - X):
                nearest1 = i

        for i in reversed(sorted_lst):
            if abs(i - X) < abs(nearest2 - X):
                nearest2 = i

        if nearest1 == nearest2:
            print(f'Ближайшее значение: {nearest1}')
        else:
            print(f'Ближайшие значения: {nearest1} и {nearest2}')
        print()
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
