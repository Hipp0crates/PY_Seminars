# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число).
# Input: 5
# Output: yes

def prime_number(n, m):
    if n == 1 or m == 1:
        return 'Простое'
    elif n % m == 0:
        return 'Нет'
    else:
        return 'Простое' and prime_number(n, m-1)


try:
    while True:
        n = int(input('Введите число: '))
        print(prime_number(n, n-1))
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
