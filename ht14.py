# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
#  не превосходящие числа N. 10 -> 1 2 4 8

N = int(input('Введите число: '))
x = 1

for i in range(1,N):
   x = x*2
   if x<N:
    print(x, end = ' ')
