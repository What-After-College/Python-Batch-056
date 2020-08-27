from itertools import permutations

word, r = input().split()
r = int(r)

pr = permutations(list(word), r)

ans = []
for i in pr:
    temp = ''.join(list(i))
    ans.append(temp)
ans.sort()
print(*ans, sep="\n")