dic = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    dic[name] = score
maxi = 1000
maxi1 = 1000
for i,j in dic.items():
    if maxi>j:
        maxi = j
for i,j in dic.items():
    if maxi1>j and j!=maxi:
        maxi1 = j
arr = []
for i,j in dic.items():
    if j==maxi1:
        arr.append(i)
arr.sort()
for i in arr:
    print(i)
