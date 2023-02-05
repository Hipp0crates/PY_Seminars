# Требуется вывести все целые степени двойки(т.е. числа вида 2^k), не превосходящие числа N.

try:
    while True:
        N = int(input('Целые степени двойки не больше числа: '))
        square = 0
        count = 0
        while square <= N:
            square = 2**count
            if square <= N:
                print(f'{square}', end=' ')
            count += 1
        print()
except:
    print('Введены некорректные данные.\n'
          'Выход из программы.')
exit()
