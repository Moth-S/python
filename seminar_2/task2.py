# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Запрещено использовать функцию factorial из библиотеки math


n = int(input('N = '))
product = 1
strng = []


for i in range(1, n+1):
    product *= i
    strng.append(product)


print(strng)
