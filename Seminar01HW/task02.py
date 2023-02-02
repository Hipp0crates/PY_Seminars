# HARD MOD
# Найдите сумму цифр любого вещественного или целого числа.
# Можно использовать decimal. Через строку решать нельзя.

from decimal import *
getcontext().prec = 15
try:
    while True:
        number = Decimal(float(input('Введите число: ')))

        sum = 0
        if number < 0:
            number = -number
        if number % 1 != 0:
            while number % 1 != 0:
                number *= 10
        while number > 0:
            digit = int(number % 10)
            sum += digit
            number //= 10
        print(f'Сумма цифр в числе = {sum}')
except:
    print('Введены некорректные данные')
exit()
