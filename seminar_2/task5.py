# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

from random import randint


def mixing_elements(lst):
    lst2=lst[:]
    lst1 = []

    while len(lst2) > 0:

        n = randint(0, len(lst2) - 1)
        lst1.append(lst2[n])
        lst2.pop(n)

    lst=lst1       
    return lst


N = 10
lst = [randint(-N, N) for i in range(N)]


print(lst)
print(mixing_elements(lst))
print(mixing_elements(lst))


