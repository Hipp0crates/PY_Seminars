from json import *

buttons = {
    '1': 'Добавить',
    '2': 'Удалить',
    '3': 'Словарь',
    '5': 'Сохранить',
    '8': 'Случайное',
    '*': 'Завершить',
    '#': 'Магия Нехогвардс',
}

try:
    with open('words.json', 'r', encoding='utf-8') as sl:
        words = load(sl)
except:
    words = {
        'hello': 'привет',
        'world': 'мир'
    }
