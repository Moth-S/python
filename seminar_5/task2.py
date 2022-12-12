
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint

n=2021
first = randint(1,10)
print(first)


while n>28:
    if first%2==0: 
        
        print('\n computer goes ')
        if n%29==0:
            b=29-b
            n-=b
        else:
            b=n%29
            n-=b
        print(f'step {b}-> balance: {n}')
        
    else:
        print('\n user goes ')
        b = int(input())
        if b<29:
            n-=b
            print(f'step {b}-> balance: {n}')
        else:
            print('error!')
            first-=1
    first+=1

if first%2==0:
    print('computer win ')
else:
    print('user win ')
        
