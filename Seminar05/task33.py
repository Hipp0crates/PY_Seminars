# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint


def change_grades(grades, i=0):
    if i == len(grades):
        return grades
    else:
        if grades[i] > 3:
            grades[i] -= 3
    return change_grades(grades, i+1)


try:
    while True:
        n = int(input('Введите количество оценок: '))
        grades = [randint(1, 5) for _ in range(n)]
        print(grades)
        print(change_grades(grades))
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
