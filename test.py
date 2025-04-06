from collections import defaultdict
from lines import starting_time, line

n = 10

V = set()
for i in range(n):
    for j in range(n):
        V.add((i,j))

E = set()
for x, y in V:
    temp = []
    if x > 0:
        temp.append((x - 1, y))
    if x < n - 1:
        temp.append((x + 1, y))
    if y > 0:
        temp.append((x, y - 1))
    if y < n - 1:
        temp.append((x, y + 1))
    for t in temp:
        E.add(((x, y), t, 1))

H = defaultdict(list)

for l in range(len(line)):
    for i in range(len(line[l])):
        v, f = line[l][i]
        if f == 1:
            for st in starting_time[l]:
                H[v].append((l, st + i))

for h in H.items():
    print(h)