# Вычислить число π c заданной точностью d

# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = float(input("round pi to the nearest - > "))

i=1
count=0
step = 0
num_pi=0
while abs((pi-num_pi*4))>d:
    if step%2==0:
        num_pi+=1/i
    else:
        num_pi-=1/i
    print(num_pi*4)   
    count+=1
    step+=1
    i+=1
print(count)
print(f"{round(4*num_pi,3)} - {round(pi,3)} = {abs(4*num_pi-pi)}" )   
    






