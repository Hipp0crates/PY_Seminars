# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массива.

from random import randint
try:
    N = int(input('Введите количество элементов: '))
    lst = [randint(1, 9) for _ in range(N)]
    while True:
        print(f'Задан массив: {lst}')
        X = int(input('Введите число от 1 до 9: '))
        if X < 1 or X > 9:
            print('Нет такого числа в массиве.')
            print()
            continue

        count = 0
        for i in lst:
            if i == X:
                count += 1
        print(f'Количество совпадений: {count}')
        print()
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
