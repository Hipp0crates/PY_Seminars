import functions as f
import dictionaries as d
from os import system

system('cls')
print('Телефонный справочник запущен')

while True:
    cmd = input(
        '1(Добавить) 2(Удалить) 3(Изменить) 7(Контакты) 8(Сохранить) 9(Выход) 0(Прерывание): ')
    if cmd == '#':
        f.buttons()
    elif cmd == '1':
        f.add_contact()
    elif cmd == '2':
        f.remove_contact()
    elif cmd == '3':
        f.edit_contact()
    elif cmd == '7':
        f.show_contacts()
    elif cmd == '8':
        f.save_contacts()
    elif cmd == '9':
        f.save_contacts()
        print('ВЫХОД')
        break
    elif cmd == '0':
        print('ВЫХОД БЕЗ СОХРАНЕНИЯ')
        break
    else:
        f.buttons()
