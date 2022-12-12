# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

def arch(s):
    strng=''
    count=1
    for i in range(1,len(s)):
        if s[i-1]==s[i] and count<9: count+=1
        else:
            strng=strng+str(count)+s[i-1]
            count=1
    return strng

def unarch(s):
    strng=''
    c=0
    for i in range(0,len(s),2):
        c=int(s[i])
        strng=strng+c*s[i+1]
    return strng


with open('seminar_5/1.txt') as file:
    text=str(file.readline())
    text2=arch(text+' ')
    print(f'{text} -> {text2}')
    file.close

file = open('seminar_5/2.txt','w')
file.write(text2)
file.close()

with open('seminar_5/2.txt') as file:
    text=str(file.readline())
    text3=unarch(text)
    print(f'{text} -> {text3}')
    file.close

file = open('seminar_5/1.txt','w')
file.write(text3)
file.close()
