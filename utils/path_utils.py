from copy import deepcopy


def beautify_path(path):

    cleared_path = [path[0]]

    for i in range(1, len(path) - 1) :
        if path[i-1][0] == path[i][0] == path[i+1][0] :
            continue
        # if path[i-1][2] == path[i][2] == path[i+1][2] :
        #     continue
        if path[i][0] == cleared_path[-1][0] and len(cleared_path) == 1 :
            cleared_path.pop()

        cleared_path.append(path[i])
    cleared_path.append(path[-1])

    return cleared_path