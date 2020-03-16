x = int(input())
cnt = 0
arr = list(map(int, input().split()))
for i in arr:
    if i>0:
        cnt+=1
print(cnt)