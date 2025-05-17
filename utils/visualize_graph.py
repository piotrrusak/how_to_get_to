import pygame
from collections import defaultdict
import math

def nested_defaultdict(depth = 1, default_value = None):
    if depth == 1:
        return defaultdict(default_value)
    return defaultdict(lambda: nested_defaultdict(depth - 1, default_value))


MARGIN = 100

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 2000

BASE_LINE_WIDTH = 5
WIDTH_MULTIPLIER = 2

BASE_CIRCLE_RADIUS = 10
COLORED_CIRCLE_RADIUS = BASE_CIRCLE_RADIUS * WIDTH_MULTIPLIER

COLORED_LINE_WIDTH = BASE_LINE_WIDTH * WIDTH_MULTIPLIER

DIM_FACTOR = 0.3

def dim_color(color, factor = DIM_FACTOR) :
    return (int(color[0] * factor), int(color[1] * factor), int(color[2] * factor))

def visualize_map(lines, colors, path = None):
    global SCREEN_WIDTH, SCREEN_HEIGHT, MARGIN
    global BASE_LINE_WIDTH, COLORED_LINE_WIDTH, DIM_FACTOR

    xs, ys = zip(*(point for line in lines for point, _ in line))
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x
    height = max_y - min_y

    if width > height :
        SCREEN_HEIGHT = int(SCREEN_WIDTH * (height / width))
    elif height > width :
        SCREEN_WIDTH = int(SCREEN_HEIGHT * (width / height))


    cell_size = min(SCREEN_WIDTH // width, SCREEN_HEIGHT // height)
    
    SCREEN_WIDTH += 2 * MARGIN
    SCREEN_HEIGHT += 2 * MARGIN

    width += 1
    height += 1
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Path Visualization")

    static_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    static_image.fill((0, 0, 0))

    grid_lines = nested_defaultdict(2, lambda : [[], []])

    grid_points = nested_defaultdict(1, lambda : [[], []])

    no_dimming_condition = path is None

    for i in range(len(lines)) :
        prev = lines[i][0]
        if prev[1] == 1 :
            grid_points[prev[0]][0].append(i)
            if no_dimming_condition :
                grid_points[prev[0]][1].append(i)

        for j in range(1, len(lines[i])) :
            point = lines[i][j]
            if point[1] == 1 :
                grid_points[point[0]][0].append(i)
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
        if len(grid_points[point][0]) > 0 :
            draw_pizza(static_image,
                       (x * cell_size + MARGIN, y * cell_size + MARGIN),
                       COLORED_CIRCLE_RADIUS,
                       len(grid_points[point][0]),
                       [colors[i] for i in grid_points[point][0]],
                       [colors[i] for i in grid_points[point][1]])
        else :
            pygame.draw.circle(static_image, dim_color((255, 255, 255)), (x * cell_size + MARGIN, y * cell_size + MARGIN), BASE_CIRCLE_RADIUS)

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
                
                x1 = point_1[0] * cell_size + MARGIN + (k * colored_width / 2 if is_vertical else 0)
                y1 = point_1[1] * cell_size + MARGIN + (0 if is_vertical else k * colored_width / 2)
                x2 = point_2[0] * cell_size + MARGIN + (k * colored_width / 2 if is_vertical else 0)
                y2 = point_2[1] * cell_size + MARGIN + (0 if is_vertical else k * colored_width / 2)
                
                pygame.draw.line(
                    static_image,
                    color if color_id in important_colors else dim_color(color),
                    (x1, y1),
                    (x2, y2),
                    colored_width
                )
                i += 1
        else :
            pygame.draw.line(static_image, dim_color((255, 255, 255)),
                                (point_1[0] * cell_size + MARGIN, point_1[1] * cell_size + MARGIN),
                                (point_2[0] * cell_size + MARGIN, point_2[1] * cell_size + MARGIN),
                                BASE_LINE_WIDTH)
    
    if not no_dimming_condition :
        prev_point = path[0][0]
        prev_color_code = path[0][1]


        for i in range(1, len(path)) :
            entry = path[i]
            point, _ = entry

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