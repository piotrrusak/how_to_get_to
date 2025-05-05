from collections import defaultdict

def load_harmonogram(lines, starting_times):
    H = defaultdict(list)

    for l in range(len(lines)):
        for i in range(len(lines[l])):
            v, f = lines[l][i]
            if f == 1:
                for st in starting_times[l]:
                    H[v].append((l, st + i, ))