L1 = [ # Red
    ((0, 0), True),
    ((0, 1), False),
    ((1, 1), False),
    ((1, 2), False),
    ((1, 3), True),
    ((2, 3), False),
    ((3, 3), False),
    ((4, 3), True),
    ((4, 4), False),
    ((4, 5), False),
    ((4, 6), True),
    ((5, 6), False),
    ((6, 6), False),
    ((6, 5), True),
    ((7, 5), False),
    ((7, 6), False),
    ((7, 7), False),
    ((8, 7), True),
    ((8, 8), False),
    ((8, 9), False),
    ((9, 9), True),
]

L2 = [ # Blue
    ((0, 9), True),
    ((1, 9), False),
    ((1, 8), False),
    ((1, 7), True),
    ((2, 7), False),
    ((3, 7), False),
    ((4, 7), False),
    ((4, 6), True),
    ((5, 6), False),
    ((5, 5), False),
    ((5, 4), False),
    ((5, 3), False),
    ((5, 2), False),
    ((5, 1), False),
    ((5, 0), True),
    ((6, 0), False),
    ((7, 0), False),
    ((8, 0), False),
    ((9, 0), True)
]

L3 = [ # Green
    ((0, 5), True),
    ((1, 5), False),
    ((2, 5), True),
    ((3, 5), False),
    ((4, 5), False),
    ((4, 6), True),
    ((5, 6), False),
    ((6, 6), False),
    ((6, 5), True),
    ((7, 5), False),
    ((8, 5), False),
    ((8, 4), False),
    ((8, 3), True),
    ((8, 2), False),
    ((9, 2), True),
]

L4 = [ # Yellow
    ((7, 9), True),
    ((6, 9), False),
    ((5, 9), False),
    ((4, 9), True),
    ((4, 8), False),
    ((4, 7), False),
    ((4, 6), True),
    ((4, 5), False),
    ((4, 4), False),
    ((4, 3), True),
    ((4, 2), False),
    ((4, 1), False),
    ((3, 1), True),
    ((3, 0), False),
    ((2, 0), True),
]

starting_times = [
    [0, 5, 10],
    [0, 6, 12],
    [0, 7, 14],
    [0, 8, 16],
]

lines = [L1, L2, L3, L4]
colors = [
    (255, 0, 0),  # Red
    (0, 0, 255),  # Blue
    (0, 255, 0),  # Green
    (255, 255, 0),  # Yellow
]