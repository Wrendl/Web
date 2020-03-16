x = int(input())
y = int(input())
z = int(input())
n = int(input())
list = []
ll = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                list.append(i)
                list.append(j)
                list.append(k)
                ll.append(list.copy())
                list.pop()
                list.pop()
                list.pop()
print(ll)