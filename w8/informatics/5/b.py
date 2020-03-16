def f(x,y):
    ans = 1
    for i in range(y):
        ans*=x
    print(ans)
a = list(map(int,input().split()))
f(a[0],a[1])