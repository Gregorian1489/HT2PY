n = int(input('Введите количество арбузов: '))

max = 0
min = 100
for i in range(n):
    mass = int(input())
    if mass > max:
        max = mass
    if mass < min:
        min = mass
print(f'Максимальная масса арбуза = {max}, минимальная = {min}')        