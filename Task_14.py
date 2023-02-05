""" Задача 14:
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример :
10 -> 1 2 4 8  """

N = int(input('Введите число-ограничитель: '))
degrees = []
count = 1
while count <= N:
    degrees.append(count)
    count *= 2
print(*degrees)
