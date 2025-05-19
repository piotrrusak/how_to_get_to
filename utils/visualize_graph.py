import pygame
from collections import defaultdict
import math

def nested_defaultdict(depth = 1, default_value = None):
    if depth == 1:
        return defaultdict(default_value)
    return defaultdict(lambda: nested_defaultdict(depth - 1, default_value))


MARGIN = 20

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 2000


BASE_CIRCLE_RADIUS = 4
WIDTH_MULTIPLIER = 2

BASE_LINE_WIDTH = BASE_CIRCLE_RADIUS // 2

COLORED_CIRCLE_RADIUS = BASE_CIRCLE_RADIUS * WIDTH_MULTIPLIER

COLORED_LINE_WIDTH = BASE_LINE_WIDTH * WIDTH_MULTIPLIER

DIM_FACTOR = 0.3

def dim_color(color, factor = DIM_FACTOR) :
    return (int(color[0] * factor), int(color[1] * factor), int(color[2] * factor))

def visualize_map(lines, colors, path = None):
    global SCREEN_WIDTH, SCREEN_HEIGHT, MARGIN
    global BASE_LINE_WIDTH, COLORED_LINE_WIDTH, DIM_FACTOR
    global BASE_CIRCLE_RADIUS, COLORED_CIRCLE_RADIUS

    xs, ys = zip(*(point for line in lines for point, _ in line))
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    SCREEN_WIDTH -= 2 * MARGIN
    SCREEN_HEIGHT -= 2 * MARGIN

    if width > height :
        SCREEN_HEIGHT = int(SCREEN_WIDTH * (height / width))
    elif height > width :
        SCREEN_WIDTH = int(SCREEN_HEIGHT * (width / height))

    cell_size = min(SCREEN_WIDTH / (width - 1), SCREEN_HEIGHT / (height - 1))


    SCREEN_WIDTH = 2 * MARGIN + int(cell_size * (width - 1))
    SCREEN_HEIGHT = 2 * MARGIN + int(cell_size * (height - 1))


    if BASE_CIRCLE_RADIUS > (cell_size // 2) :
        BASE_CIRCLE_RADIUS = int(cell_size // 2)
        COLORED_CIRCLE_RADIUS = BASE_CIRCLE_RADIUS * WIDTH_MULTIPLIER
        BASE_LINE_WIDTH = BASE_CIRCLE_RADIUS // 2
        COLORED_LINE_WIDTH = BASE_LINE_WIDTH * WIDTH_MULTIPLIER

    def get_point_location(point) :
        x, y = point
        return (int(x * cell_size) + MARGIN, int(y * cell_size) + MARGIN)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Path Visualization")

    static_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    static_image.fill((0, 0, 0))

    grid_lines = nested_defaultdict(2, lambda : [[], []])

    grid_points = nested_defaultdict(1, lambda : [[], [], False])

    no_dimming_condition = path is None

    for i in range(len(lines)) :
        prev = lines[i][0]
        grid_points[prev[0]][0].append(i)
        if prev[1] :
            grid_points[prev[0]][2] = True
            if no_dimming_condition :
                grid_points[prev[0]][1].append(i)

        for j in range(1, len(lines[i])) :
            point = lines[i][j]
            grid_points[point[0]][0].append(i)
            if point[1] :
                grid_points[point[0]][2] = True
                if no_dimming_condition : 
                    grid_points[point[0]][1].append(i)
            
            grid_lines[prev[0]][point[0]][0].append(i)
            grid_lines[point[0]][prev[0]][0].append(i)
            if no_dimming_condition :
                grid_lines[prev[0]][point[0]][1].append(i)
                grid_lines[point[0]][prev[0]][1].append(i)
            prev = point

    def draw_pizza(screen, center, radius, num_slices, colors, important_colors = None) :
        if important_colors is None :
            important_colors = []
        angle_step = 360 / num_slices
        
        for i in range(num_slices) :
            start_angle = math.radians(angle_step * i)

            points = [center]
            for angle in range(int(angle_step) + 1) :
                theta = start_angle + math.radians(angle)
                x = center[0] + radius * math.cos(theta)
                y = center[1] + radius * math.sin(theta)
                points.append((x, y))
            pygame.draw.polygon(screen, colors[i] if colors[i] in important_colors else dim_color(colors[i]), points)

    def draw_point(point) :
        nonlocal static_image, grid_points, colors
        x, y = point
        # if None in grid_points[point][1] : return
        # print(point, grid_points[point])
        if len(grid_points[point][0]) > 0 or grid_points[point][2] :
            draw_pizza(static_image,
                       get_point_location(point),
                       COLORED_CIRCLE_RADIUS if grid_points[point][2] else COLORED_LINE_WIDTH / 2,
                       len(grid_points[point][0]),
                       [colors[i] for i in grid_points[point][0]],
                       [colors[i] for i in grid_points[point][1]])
        # else :
        #     pygame.draw.circle(static_image, dim_color((255, 255, 255)), (x * cell_size + MARGIN, y * cell_size + MARGIN), BASE_CIRCLE_RADIUS)

    def draw_line(point_1, point_2) :
        important_colors = grid_lines[point_1][point_2][1]
        n = len(grid_lines[point_1][point_2][0])
        if n > 0 :
            colored_width = COLORED_LINE_WIDTH
            if colored_width*n > 2*COLORED_CIRCLE_RADIUS :
                colored_width = 2*COLORED_CIRCLE_RADIUS/n

            i = 0
            for k in range(1 - n, n, 2) :
                color_id = grid_lines[point_1][point_2][0][i]
                color = colors[color_id]
                is_vertical = point_2[0] == point_1[0]

                x1, y1 = get_point_location(point_1)
                x2, y2 = get_point_location(point_2)
                if is_vertical :
                    x1 += k * colored_width / 2
                    x2 += k * colored_width / 2
                else :
                    y1 += k * colored_width / 2
                    y2 += k * colored_width / 2
                
                pygame.draw.line(
                    static_image,
                    color if color_id in important_colors else dim_color(color),
                    (x1, y1),
                    (x2, y2),
                    int(colored_width)
                )
                i += 1
        else :
            pygame.draw.line(static_image, dim_color((255, 255, 255)),
                                (point_1[0] * cell_size + MARGIN, point_1[1] * cell_size + MARGIN),
                                (point_2[0] * cell_size + MARGIN, point_2[1] * cell_size + MARGIN),
                                BASE_LINE_WIDTH)

    if not no_dimming_condition :
        prev_point, prev_color_code = path[0]
        
        for i in range(1, len(path)) :
            entry = path[i]
            point, _ = entry
            # print(prev_color_code)

            if point != prev_point :
                grid_lines[prev_point][point][1].append(prev_color_code)
                grid_lines[point][prev_point][1].append(prev_color_code)
            grid_points[prev_point][1].append(prev_color_code)

            prev_point, prev_color_code = entry
        grid_points[prev_point][1].append(prev_color_code)


    for x in range(width) :
        for y in range(height) :
            edges = [(x-1, y), (x, y-1)]
            for edge in edges :
                if edge[0] < 0 or edge[1] < 0 or edge[0] >= width or edge[1] >= height :
                    continue
                draw_line((x, y), edge)

    for x in range(width):
        for y in range(height):
            draw_point((x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(static_image, (0, 0))
        pygame.display.update()

    pygame.quit()