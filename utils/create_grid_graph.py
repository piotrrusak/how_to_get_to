def create_grid_graph(n):
    V = set()
    for i in range(n):
        for j in range(n):
            V.add((i, j))

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

    return V, E