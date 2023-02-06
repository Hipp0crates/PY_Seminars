# Пользователь вводит текст (строка).
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
str = '''She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells.'''
# Output: 13

znaki = ['.', ',', ';']
for z in znaki:
    str = str.replace(z, ' ')
str = str.replace("I'm", 'I am')
str = str.lower()
print(f'Строка после замен:\n{str}')

lst = set(str.lower().split())
print(f'Множество:\n{lst}')
print(f'Количество элементов множества: {len(lst)}')
