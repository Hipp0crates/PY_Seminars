# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к # символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

symbols = 'a a a b c a a d c d d'
print(f'Исходная строка:\n{symbols}')

catalog = symbols.split()
print(f'Список:\n{catalog}')

array = set(catalog)
print(f'Множество:\n{array}')

score = 0
for i in array:
    for j in range(0, len(catalog)):
        if i == catalog[j]:
            score += 1
            if score >= 2:
                catalog[j] = catalog[j] + '_' + str(score - 1)
    score = 0
print('Результирующая строка:')
print(' '.join(catalog))
