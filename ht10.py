# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть.

n = int(input('Введите количество монеток: '))
print('0 - реверс, 1 - аверс, через Enter')
count_0 = 0
count_1 = 0

for i in range(n):
    cent = int(input())
    if cent !=0 and cent !=1:
        print ('Вводим только 1 или 0 !')
        break
    if cent == 0:
        count_0 += 1
    if cent == 1:
        count_1 += 1
if count_0 < count_1 and count_0 != 0:
    print (f'Нужно перевернуть {n - count_1} монеток')
if count_1 < count_0 and count_1 != 0:
    print (f'Нужно перевернуть {n - count_0} монеток')
if count_0 == count_1 and count_0 != 0:
    print (f'Нужно перевернуть {count_0} монеток')
else:
    print ('Ничего переворачивать не надо')