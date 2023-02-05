# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов списка, больших предыдущего (элемента с предыдущим номером).
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint
n = int(input('Введите количество элементов списка: '))
lst = [randint(-10, 10) for _ in range(n)]
print(lst)

count = 0
for i in range(1, len(lst)):
    if lst[i-1] < lst[i]:
        count += 1
        print(f'{count}. ({lst[i-1]} < {lst[i]})')
print(f'Количество элементов списка больше предыдущего: {count}')
