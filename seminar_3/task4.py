# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_number(num):
    strng = ''
    while num > 0:
        strng += str(num % 2)
        num //= 2

    return strng


number = int(input("number: "))
print(f"{number} => {binary_number(number)}")
