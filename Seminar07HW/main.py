import functions as f
import dictionaries as d

f.show(d.buttons)

while True:
    cmd = input('Ваш символ ("0" для помощи): ')
    if cmd == '0':
        f.show(d.buttons)
    elif cmd == '1':
        f.add(d.words)
    elif cmd == '2':
        f.remove(d.words)
    elif cmd == '3':
        f.show(d.words)
    elif cmd == '5':
        f.save(d.words)
    elif cmd == '8':
        f.random(d.words)
    elif cmd == '*':
        f.save(d.words)
        print('ВЫХОД')
        break
    elif cmd == '#':
        f.magic()
    else:
        f.show(d.buttons)
