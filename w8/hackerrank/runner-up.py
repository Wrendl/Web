n = int(input())
arr = list(map(int,input().split()))
maxi = -101
maxi1 = -101
for i in range(n):
    if maxi<arr[i]:
        maxi = arr[i]
for i in range(n):
    if maxi1<arr[i] and maxi!=arr[i]:
        maxi1 = arr[i]
print(maxi1)