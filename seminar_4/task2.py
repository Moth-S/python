# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# *Пример*
# - при N=236     ->        [2, 2, 59]

N = int(input('N = '))

s = []


for i in range(2, N+1):
    if N % i == 0:
        print(N)
        s.append(i)
        N = N//i
        i = 2
s.append(N)

print(sorted(s))
