# Напишите программу, удаляющую из файла все слова, содержащие "абв".
with open("seminar_5/3.txt",'a') as file:
    file.write(input())
    file.close

with open("seminar_5/3.txt") as file:
    text=file.readline().split()
    print(text)
    
    text1=list(filter(lambda i: 'абв' not in i, text))
    
    print(text1)
    file.close


    
my_file=open("seminar_5/3.txt",'w')
my_file.write(' '.join(text1))

    

