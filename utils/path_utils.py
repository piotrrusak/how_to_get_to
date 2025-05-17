from copy import deepcopy


def beautify_path(path):

    cleared_path = [path[0]]

    for i in range(1, len(path) - 1) :
        if path[i-1][0] == path[i][0] == path[i+1][0] :
            continue
        if path[i-1][2] == path[i][2] == path[i+1][2] and path[i][0] != path[i-1][0] and path[i][0] != path[i+1][0] :
            continue
        if path[i][0] == cleared_path[-1][0] and len(cleared_path) == 1 :
            cleared_path.pop()

        cleared_path.append(path[i])
    cleared_path.append(path[-1])

    return cleared_path

def find_full_path(path, lines) :
    full_path = []

    path_parts = []

    for i in range(0, len(path), 2) :
        path_parts.append([path[i], path[i+1]])
    for part in path_parts :
        start_point, _, line = part[0]
        end_point = part[1][0]
        add = False
        for point in lines[line] :
            if point[0] == start_point :
                add = True
            if add :
                full_path.append((point[0], line))
            if point[0] == end_point :
                break

    return full_path