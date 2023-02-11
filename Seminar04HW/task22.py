# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from os import system


def data_input(size):
    sp = []
    for i in range(size):
        sp.append(int(input(f'Введите число {i+1}: ')))
    return (sp)


def print_duplicates(sp1, sp2):
    sp1 = set(list(sp1))
    sp2 = set(list(sp2))
    sp = []
    for i in sp1:
        for j in sp2:
            if i == j:
                sp.append(i)
    print('Повторяющиеся значения:', *sp)


try:
    system('cls')
    while True:
        n = int(input('Введите количество элементов первого множества: '))
        lst_n = data_input(n)
        m = int(input('Введите количество элементов второго множества: '))
        lst_m = data_input(m)
        print(f'Первое множество:', *lst_n)
        print(f'Второе множество:', *lst_m)
        print_duplicates(lst_n, lst_m)
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
