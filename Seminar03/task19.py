# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint

n = int(input('Введите количество элементов списка: '))
k = int(input('На сколько сдвинуть сдвинуть всю последовательность вправо: '))
lst = [randint(-10, 10) for _ in range(n)]
print(lst)

for i in range(k):
    lst.insert(0, lst.pop())
print(lst)

# Удалить отрицательные значения
lst = [i for i in lst if i >= 0]
print(lst)
