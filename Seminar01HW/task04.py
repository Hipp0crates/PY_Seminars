# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

try:
    while True:
        s = int(input('Введите количество журавликов: '))
        if s % 6 != 0:
            print('Введите число кратное 6, иначе дети наделают недоделанных журавликов.\n'
                'По условию не заданно как считать частично сделанные журавлики.')
            print(f'Петя сделал {round(s/6, 2)}\n'
                f'Катя сделала {round(s*4/6, 2)}\n'
                f'Сережа сделал {round(s/6, 2)}')
        else:
            print(f'Петя сделал {s//6}\n'
                f'Катя сделала {s*4//6}\n'
                f'Сережа сделал {s//6}')
except:
    print('Введены некорректные данные')
exit()