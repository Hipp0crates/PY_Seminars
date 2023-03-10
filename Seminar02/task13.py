# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50.

from random import randint

while True:
    N = int(input('Введите число дней или "Q" для выхода: '))

    if N == 'Q':
        exit()

    sp = []

    for i in range(N):
        x = randint(-50, 50)
        sp.append(x)
    print(sp)

    count_max = count = 0

    for i in range(N):
        if sp[i] > 0:
            count += 1
            if count_max < count:
                count_max = count
        else:
            count = 0
    print(count_max)
