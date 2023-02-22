from decimal import *
from math import *
from time import *
from random import *
from json import *
from os import system


def save(glossary):
    with open('words.json', 'w', encoding='utf-8') as gw:
        gw.write(dumps(glossary, ensure_ascii=False))
        print('Файл words.json сохранен')


def show(glossary):
    system('cls')
    for k, v in glossary.items():
        print(k, '-', v)


def add(glossary):
    system('cls')
    k = input('Введите английское слово: ')
    v = input('Введите перевод на русский: ')
    glossary[k] = v


def remove(glossary):
    system('cls')
    show(glossary)
    k = input('Введите первичное слово из списка для удаления: ')
    if k in glossary:
        del glossary[k]
    else:
        print('Нет такого слова')


def random(glossary):
    system('cls')
    k = choice(list(glossary.keys()))
    print(f'Случайное английское слово: {k}')
    v = input('Введите перевод на русский: ')
    if v in glossary.values():
        print('Верно')
    else:
        print('Не верно')


def magic():
    while True:
        system('cls')
        x = randint(2, 100)
        y = Decimal(sqrt(x))
        if y % 1 != 0:
            y = round(y, 4)
        print('Ваш звонок очень важен для нас\n'
              'Вместо музыки бесконечно смотрим на квадратные корни чисел от 2 до 100\n'
              'Просто автор этого бота не знает как выйти из бесконечного цикла')
        print(f'√{x} = {y}')
        sleep(2)
