# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(number, power):
    if power == 0:
        return 1
    elif power == 1:
        return number
    elif power == -1:
        return 1/number
    elif power < 0:
        power = abs(power)
        return 1/(number*exponentiation(number, power-1))
    else:
        return number*exponentiation(number, power-1)


try:
    while True:
        A = int(input('Введите число A: '))
        B = int(input('Введите число B: '))
        print(f'{A}^({B}) = {exponentiation(A, B)}')
        print()
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
