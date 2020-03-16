def f(a,b,c,d):
    y = a
    if y>b:
        y = b
    if y>c:
        y = c
    if y>d:
        y = d
    print(y)
arr = list(map(int,input().split()))
f(arr[0],arr[1],arr[2],arr[3])