# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

float_lst = []


for i in range(6):
    float_lst.append(round(uniform(0, 20.5), 2))


max_remainder = 0
min_remainder = 0.999


for j in float_lst:

    if j - int(j) > max_remainder:
        max_remainder = j - int(j)

    if 0 < j - int(j) < min_remainder:
        min_remainder = j - int(j)


print(f"{float_lst} => {round(max_remainder-min_remainder,2)}")
