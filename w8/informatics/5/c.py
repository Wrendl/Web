def f(x,y):
    if x==y:
        return 0
    else:
        return 1
a = list(map(int,input().split()))
print(f(a[0],a[1]))