# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*
# - 6782 -> 23
# - 0.56 -> 11

number = input('real number: ')
strng = []


for i in number:
    if i not in ('.-'):
        strng.append(int(i))

        
print(sum(strng))
