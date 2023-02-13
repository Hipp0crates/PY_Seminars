# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел.
# Все числа списка находятся на разных строках.

# a = list(map(int, input('Введите числа списка через пробел: ').split()))
# counter = 0
# a1 = set(a)
# a2 = []
# for i in (a1):
#     for j in range(0, len(a)):
#         if i == a[j]:
#             counter += 1
#     a2.append(counter)
#     counter = 0
# counter2 = 0
# for i in range(len(a2)):
#     counter2 = counter2 + a2[i]//2
# print(counter2)

from random import randint


def get_pairs(sp):
    count = 0
    for i in range(len(sp)):
        for j in range(i+1, len(sp)):
            if sp[i] == sp[j] and sp[j] != '' and sp[i] != '':
                count += 1
                sp[j] = ''
                sp[i] = ''
    print(f'Количество пар: {count}')


try:
    while True:
        n = int(input("Введите длину списка: "))
        lst = [randint(1, 9) for _ in range(n)]
        print(lst)
        get_pairs(lst)
        print()
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
