# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

lst = []
summa = 0


for i in range(6):
    lst.append(randint(-10, 10))


for j in range(len(lst)):
    if j % 2:
        summa += lst[j]


print(lst, f"\n sum of elements in odd positions: {summa}")
