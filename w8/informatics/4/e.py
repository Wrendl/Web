x = int(input())
cnt = 0
arr = list(map(int, input().split()))
for i in range(1,x):
    if arr[i]>=0 and arr[i-1]>=0:
        print("YES")
        exit(0)
    elif arr[i]<0 and arr[i-1]<0:
        print("YES")
        exit(0)
print("NO")