# Создайте программу для игры в "Крестики-нолики".

# Вариант интерфейса:

#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9

def p(strng):
    for i in strng:
        print(*i, sep=" _|_ " )
    return

def f(strng, n, symb):
    for j in range(3):
        if n in strng[j]:
            lst=strng[j]
            for i in range(3):
                if lst[i]==n:
                    lst[i]=symb
                    strng[j]=lst
    return strng

def win(lst, symb, num_pl):
    lst1,lst2,lst3 = lst[0],lst[1],lst[2]

    if lst1.count(symb)==3 or lst2.count(symb)==3 or lst3.count(symb)==3:
        flag=True
        print(f'player {num_pl} win')
        return flag

    elif lst1[0]==lst2[0]==lst3[0] or lst1[1]==lst2[1]==lst3[1] or lst1[2]==lst2[2]==lst3[2]:
        flag=True
        print(f'player {num_pl} win')
        return flag 

    elif lst1[0]==lst2[1]==lst3[2] or lst1[2]==lst2[1]==lst3[0]:
        flag=True
        print(f'player {num_pl} win')
        return flag

print("Игра 'Крестики-нолики' \n")
print("player_1 ходит крестиками 'X' \nplayer_2 ходит ноликами 'O' \n")
strng=[['1','2','3'],['4','5','6'],['7','8','9']]
step=0
flag=False


print("Выбери позицию, куда хочешь поставить свой знак: ")
p(strng)

for i in range(9):

    

    if step%2==0:
        flag=win(strng,'X', 1)
        if flag: break
        print('player_1: ')
        position=(input())
        strng=f(strng,position,'X')
        p(strng)
        step+=1
    else:
        flag=win(strng,'X', 1)
        if flag: break
        print('player_2: ')
        position = input()
        strng=f(strng,position,'O')
        p(strng)
        step+=1

