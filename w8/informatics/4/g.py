x = int(input())
cnt = 0
arr = list(map(int, input().split()))
for i in range(x):
    print(arr[x-i-1],end=' ')