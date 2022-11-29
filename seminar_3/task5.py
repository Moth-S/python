# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Negafibonacci(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num < 0:
        return (-1) ** (num + 1) * Negafibonacci(num * (-1))
    else:
        return Negafibonacci(num - 1) + Negafibonacci(num - 2)


n = int(input("number = "))
lst = []


for i in range(-n, n + 1):
    lst.append(int(Negafibonacci(i)))
print(lst)
