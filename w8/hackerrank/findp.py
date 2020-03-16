n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
ll = student_marks[query_name]
avg = (ll[0]+ll[1]+ll[2])/3
print("{0:.2f}".format(avg))