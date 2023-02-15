# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только + 1 и - 1.
# Также нельзя использовать циклы.

def recursion_sum(number1, number2):
    if number1 == 0:
        return number2
    elif number1 < 0:
        return recursion_sum(number1+1, number2)-1
    else:
        return recursion_sum(number1-1, number2)+1


try:
    while True:
        A = int(input('Введите число A: '))
        B = int(input('Введите число B: '))
        if B < 0:
            print(f'{A} - {-B} = {recursion_sum(A, B)}')
        else:
            print(f'{A} + {B} = {recursion_sum(A, B)}')
        print()
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
