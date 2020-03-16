import math as m
x = int(input())
y = int(input())
for i in range(x,y+1):
    z = int(m.sqrt(i))
    if z*z == i:
        print(i)