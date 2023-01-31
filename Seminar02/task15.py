# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза.

N = int(input('Введите количество арбузов: '))
sp = []

for i in range(N):
    sp.append(int(input(f'Вес арбуза {i+1}: ')))

min = sp[0]
max = sp[0]

for i in range(N):
    if sp[i] > max:
        max = sp[i]
    if sp[i] < min:
        min = sp[i]
print(min, max)
