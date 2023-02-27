from random import *
from json import *
from sys import *
from msvcrt import *
from os import system
import dictionaries as d


def save_contacts(glossary=d.contacts):
    with open('contacts.json', 'w', encoding='utf-8') as sc:
        sc.write(dumps(glossary, ensure_ascii=False))
        print('Файл contacts.json сохранен')


def buttons(glossary=d.buttons):
    system('cls')
    for k, v in glossary.items():
        print(k, '-', v)


def show_line(line):
    for k, v in enumerate(line):
        tmp = k + 1
        print(tmp, v)


def show_contact(glossary):
    for k, v in glossary.items():
        print(k, v)


def show_contacts(number=0, glossary=d.contacts):
    if number == 0:
        system('cls')
        for k, v in enumerate(glossary):
            tmp = k + 1
            print(f'{tmp}:', glossary[k]['1'], glossary[k]['2'], glossary[k]['3'], glossary[k]['4'],
                  ' '.join(glossary[k]['5']), ' '.join(glossary[k]['6']))
    else:
        k = number - 1
        print(f'{number}:', glossary[k]['1'], glossary[k]['2'], glossary[k]['3'], glossary[k]['4'],
              ' '.join(glossary[k]['5']), ' '.join(glossary[k]['6']))


def add_contact(glossary=d.contacts):
    system('cls')
    contact = {
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': [],
        '6': []
    }
    phones = []
    emails = []
    for k, v in contact.items():
        if k == '5':
            add_list(phones, k)
            contact[k] = phones
        elif k == '6':
            add_list(emails, k)
            contact[k] = emails
        else:
            contact[k] = input(d.input_text[k])
    glossary.append(contact)
    show_contacts()


def add_list(glossary, k):
    system('cls')
    while True:
        if k == '5':
            system('cls')
            print('"ENTER" - для пропуска ввода\n'
                  '"1" - для добавления ТЕЛЕФОНА')
            key = ord(getch())
            if key == 49:
                glossary.append(input(d.input_text[k]))
            elif key == 13:
                return glossary
            else:
                continue
        elif k == '6':
            system('cls')
            print('"ENTER" - для пропуска ввода\n'
                  '"2" - для добавления ПОЧТЫ')
            key = ord(getch())
            if key == 50:
                glossary.append(input(d.input_text[k]))
            elif key == 13:
                return glossary
            else:
                continue
        else:
            return glossary


def remove_contact(glossary=d.contacts):
    system('cls')
    show_contacts(0, glossary)
    try:
        n = int(input('Введите номер контакта для удаления: ')) - 1
        if n > -1 and n < len(glossary):
            del glossary[n]
            show_contacts()
        else:
            print('Контакта с таким номером не существует')
    except:
        show_contacts()
        print('Не введен номер контакта\nИзменения не внесены')


def edit_contact(glossary=d.contacts):
    system('cls')
    show_contacts()
    try:
        n = int(input('Номер контакта для редактирования: ')) - 1
        system('cls')
        print(f'Редактирование контакта: {n+1}')
        if n > -1 and n < len(glossary):
            contact = glossary[n]
            show_contact(contact)
            try:
                line1 = int(input('Номер строки для редактирования: '))
                line1 = int(line1)
                line1_str = str(line1)
                if line1 == 5 or line1 == 6:
                    tmp = contact[line1_str]
                    show_line(tmp)
                    try:
                        line2 = int(
                            input('Номер строки для редактирования: ')) - 1
                        if line2 > -1 and line2 < len(tmp):
                            print(tmp[line2])
                            cmd = input('2(Удалить) 3(Изменить): ')
                            if cmd == '2':
                                del tmp[line2]
                                show_contacts(n + 1)
                            elif cmd == '3':
                                tmp[line2] = input(d.input_text[line1_str])
                                contact[line1_str] = tmp
                                show_contacts(n + 1)
                            else:
                                system('cls')
                                show_contacts(n + 1)
                                print('Команда не введена\nИзменения не внесены')
                        else:
                            show_contacts()
                            print(
                                'Невозможно удалить или изменить не существующую строку')
                    except:
                        system('cls')
                        show_contacts(n + 1)
                        print('Не введен номер строки\nИзменения не внесены')
                elif line1 > 0 and line1 < 5:
                    contact[line1_str] = input(d.input_text[line1_str])
                    show_contacts(n + 1)
                else:
                    show_contacts()
                    print('Невозможно удалить или изменить не существующую строку')
            except:
                system('cls')
                show_contacts(n + 1)
                print('Не введен номер строки\nИзменения не внесены')
        else:
            show_contacts()
            print('Контакта с таким номером не существует')
    except:
        system('cls')
        show_contacts(n + 1)
        print('Не введен номер контакта\nИзменения не внесены')
