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
                H[v].append((l, st + i, ))

for h in H.items():
    print(h)

graph = {}
# ((u1, v1, t1), (u2, v2, t2))
for key in H.keys():
    for i in range(1, len(H[key])):
        _, t1 = H[key][i-1]
        _, t2 = H[key][i]
        graph[((key, t1), (key, t2))] = 1

for i in range(len(line)):
    for st in starting_time[i]:
        tail = 0
        head = 1
        while head < len(line[i]):
            u, _ = line[i][tail]
            v, f = line[i][head]
            if f == 1:
                graph[(u, st+tail), (v, st+head)] = 1
                tail = head
            head += 1

for key in graph.keys():
    print(key)
