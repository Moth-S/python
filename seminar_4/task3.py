# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

from random import randint

len_lst = int(input("length list: "))
lst = []


def Rand_list():
    num = randint(1, 10)
    return num


def nonrepeating_elements(l):
    lst_nonrepit = []
    for i in range(len(l)):
        if l.count(l[i]) == 1:
            lst_nonrepit.append(l[i])
    return lst_nonrepit


for i in range(len_lst):
    lst.append(Rand_list())

print(f"{lst} -> {nonrepeating_elements(lst)}")
