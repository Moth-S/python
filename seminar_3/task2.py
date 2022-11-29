# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

lst, lst_sum_pairs = [], []
n = int(input("Length list: "))


for j in range(n):
    lst.append(randint(-10, 10))


i = 0
while i < len(lst) // 2 + len(lst) % 2:
    lst_sum_pairs.append(lst[i] * lst[len(lst) - 1 - i])
    i += 1


print(f"{lst} => {lst_sum_pairs}")
