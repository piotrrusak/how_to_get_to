from collections import defaultdict

def load_state_graph(lines, starting_times):

    n = 10
    V = set((i, j) for i in range(n) for j in range(n))

    graph = {}
    H = defaultdict(list)

    for l in range(len(lines)):
        for i in range(len(lines[l])):
            v, f = lines[l][i]
            if f == 1:
                for st in starting_times[l]:
                    H[v].append((l, st + i))

    for key in H.keys():
        H[key].sort(key=lambda x: x[1])
        for i in range(1, len(H[key])):
            _, t1 = H[key][i - 1]
            _, t2 = H[key][i]
            graph[((key, t1), (key, t2))] = t2 - t1

    for i in range(len(lines)):
        for st in starting_times[i]:
            tail = 0
            head = 1
            while head < len(lines[i]):
                u, _ = lines[i][tail]
                v, f = lines[i][head]
                if f == 1:
                    graph[((u, st + tail), (v, st + head))] = (st+head)-(st+tail)
                    tail = head
                head += 1

    return graph