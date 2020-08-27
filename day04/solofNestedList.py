marks = []
for _ in range(int(input())):
    name = input()
    mark = float(input())
    marksheet.append([name, mark])
    marks.append(mark)

m = list(set(marks))
m.sort()
m = m[1]
ans = []
for x in marksheet:
    if x[1] == m:
        ans.append(x[0])

ans.sort()
print(*ans, sep='\n')
