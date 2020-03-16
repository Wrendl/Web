import math as m
x = int(input())
cnt = 0
if x==1:
    print(1)
else:
    y = int(m.sqrt(x))
    for i in range(1,y+1):
        if x%i==0:
            cnt+=1
    cnt*=2
    if y*y==x:
        cnt-=1
    print(cnt)