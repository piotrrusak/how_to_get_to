from random import choice

def fetch_diagonals(line):
    diagonals = []
    for i, ((x, y), _) in enumerate(line[1:], 1):
        (prev_x, prev_y), _ = line[i - 1]

        dx = abs(x - prev_x)
        dy = abs(y - prev_y)

        if dx >= 2 or dy >= 2:
            raise Exception(f"Line designed improperly! dx >= 2 or dy >= 2. Current = ({x}, {y}), prev = ({prev_x}, {prev_y}). Change it manually")
        if dx == dy == 0:
            raise Exception(f"Line designed improperly! dx == dy == 0. Current = ({x}, {y}), prev = ({prev_x}, {prev_y}). Change it manually")

        if dx == dy == 1:
            diagonals.append(i)

    return diagonals

def impute(line):
    insertions = {}
    diagonals = fetch_diagonals(line)

    for i in diagonals:
        (x, y), _ = line[i]
        (prev_x, prev_y), _ = line[i - 1]

        supplements = [
            ((x, prev_y), False),
            ((prev_x, y), False)
        ]
        insertions[i] = choice(supplements)

    result = []
    n = len(line)
    i = 0

    while i < n:
        point = line[i]
        result.append(point)
        if i in insertions:
            result[-1] = insertions[i]
            result.append(point)
        i += 1

    return result

def impute_lines(lines):
    result = []
    for line in lines:
        imputed = impute(line)
        result.append(imputed)

    return result
