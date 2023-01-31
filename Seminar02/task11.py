# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n) = A.
# Если А не является числом Фибоначчи, выведите число - 1.

num = int(input('Введите натуральное число: '))
first = 0
second = 1
counter = 2

while second <= num:
    if second == num:
        print(f'{num} является {counter}-ым в последовательности Фибоначчи')
        break
    first, second = second, first + second
    counter += 1
else:
    print(f'{num} не является числом Фибоначчи')
