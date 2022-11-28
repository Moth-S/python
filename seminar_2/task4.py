# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

from random import randint


N = int(input("N = "))
lst = [randint(-N, N) for i in range(N)]


index = input("enter indexes separated by spaces -> ").split(" ")
index = [int(i) for i in index]


print(lst, f"\n {lst[index[0]]} * {lst[index[1]]} = {lst[index[0]] * lst[index[1]]}")
