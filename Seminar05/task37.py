# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def str_input(i=0, str=''):
    if i >= n:
        return str
    str += input(f'Введите символ {i+1}: ')
    return str_input(i+1, str)


def str_reverse(i, input_line, result_line=''):
    if i < 0:
        return result_line
    result_line += input_line[i]
    return str_reverse(i-1, input_line, result_line)


try:
    while True:
        n = int(input('Введите количество элементов: '))
        sequence = str_input()
        print(' '.join(sequence))
        reverse = str_reverse(len(sequence) - 1, sequence)
        print(' '.join(reverse))
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()
