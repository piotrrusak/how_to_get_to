import pygame
import storage
from copy import copy

# README XD
# w skrócie możesz sobie rysować po mapie jak w paincie, koordynaty są zapisywane w pamięci
# klawisze: S - zapisz to co narysowałeś do pliku
# D - usuń z mapy to co nabazgrałeś, F - zwiększ counter o 1 (nazwa pliku to "out_{counter}.txt")
# lewy myszki - rysuj w danym punkcie, prawy - wykasuj
# miłej zabawy

pygame.init()

clock = pygame.time.Clock()
MAP = pygame.image.load('krakow.png')
SIZE = MAP.get_size()
WINDOW_SIZE = SIZE[0] * 2, SIZE[1] * 2
WIDTH, HEIGHT = WINDOW_SIZE

SCALED_MAP = pygame.transform.scale(MAP, WINDOW_SIZE)

window = pygame.display.set_mode(WINDOW_SIZE)

SQUARE_SIZE = WIDTH // 100
PANEL_SIZE = WIDTH // 4

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
CYAN = 0, 255, 255
MAGENTA = 255, 0, 255
ORANGE = 255, 128, 0
VIOLET = 128, 0, 255
IDK_1 = 128, 255, 0
IDK_2 = 0, 255, 128
IDK_3 = 0, 128, 255
IDK_4 = 128, 128, 128
IDK_5 = 128, 0, 128
BROWN = 139, 69, 19
PINK = 255, 192, 203
LIME = 191, 255, 0
TEAL = 0, 128, 128
NAVY = 0, 0, 128
OLIVE = 128, 128, 0
TURQUOISE = 64, 224, 208
BEIGE = 245, 245, 220
SALMON = 250, 128, 114
GOLD = 255, 215, 0
SILVER = 192, 192, 192
MAROON = 128, 0, 0
SKY_BLUE = 135, 206, 235

COLORS = [
    RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE, VIOLET, IDK_1, IDK_2, IDK_3, IDK_4, IDK_5,
    BROWN, PINK, LIME, TEAL, NAVY, OLIVE, TURQUOISE, BEIGE, SALMON, GOLD, SILVER, MAROON, SKY_BLUE
]

def darkened(r, g, b, scale=0.5):
    return r * scale, g * scale, b * scale

def color_square(x, y, color, dark=False):
    rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
    color = color if not dark else darkened(*color)
    pygame.draw.rect(window, color, rect)

def save(coords, stop_mapping, filename="out.txt"):
    with open(filename, "w") as f:
        f.write("[\n")
        for x, y in coords:
            f.write(f"(({x},{y}), {stop_mapping[(x, y)]}),\n")
        f.write("]")

def main():
    run = True

    lines_storage = {}

    squares = []
    square_dict = {}
    stops = set()
    file_idx = 0
    for line in storage.storage:
        for square, stop in line:
            squares.append(square)
            square_dict[square] = stop
            if stop:
                stops.add(square)
        color = COLORS[file_idx % len(COLORS)]
        lines_storage[file_idx] = copy(squares), copy(square_dict), color
        squares = []
        square_dict = {}
        file_idx += 1

    filename = f"out_{file_idx}.txt"
    smooth_coloring = True
    stops_adding = False

    current_color = COLORS[file_idx]

    lines_storage[file_idx] = squares, square_dict, current_color

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stops_adding:
                    x, y = pygame.mouse.get_pos()
                    normalized = x // SQUARE_SIZE, y // SQUARE_SIZE
                    if event.button == pygame.BUTTON_LEFT:
                        if normalized in square_dict:
                            print(f"{normalized} is now a stop")
                            square_dict[normalized] = True
                            stops.add(normalized)
                        else:
                            print(f"{normalized} isn't on the path")
                    elif event.button == pygame.BUTTON_RIGHT:
                        purge_stop = True
                        for i, (sq, sq_dict, _) in lines_storage.items():
                            if i == file_idx: continue
                            past_stops = filter(lambda s: sq_dict[s], sq_dict.keys())
                            if normalized in past_stops:
                                purge_stop = False
                                print(f"{normalized} is still a stop in line {i}. It hasn't been removed from the stops registry")
                                break
                        if purge_stop:
                            stops.discard(normalized)
                            print(F"{normalized} isn't a stop for any line! Stop removed from the registry")
                        square_dict[normalized] = False

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_s:
                        save(squares, square_dict, filename)
                        lines_storage[file_idx] = copy(squares), copy(square_dict), current_color
                        squares = []
                        square_dict = {}
                        file_idx += 1
                        print('Coordinates saved')
                        filename = f"out_{file_idx}.txt"
                        print("File name changed to " + filename)
                        current_color = COLORS[file_idx % len(COLORS)]

                        lines_storage[file_idx] = squares, square_dict, current_color

                        smooth_coloring = True
                        stops_adding = False

                    case pygame.K_d:
                        squares.clear()
                        square_dict.clear()
                        print('Coordinates purged')
                    case pygame.K_f:
                        file_idx += 1
                    case pygame.K_SPACE:
                        smooth_coloring = not smooth_coloring
                        stops_adding = not stops_adding

        if smooth_coloring:
            x, y = pygame.mouse.get_pos()
            normalized = x // SQUARE_SIZE, y // SQUARE_SIZE
            mouse_pressed = pygame.mouse.get_pressed()

            if mouse_pressed[0] and normalized not in square_dict:
                print(f"Add {normalized}")
                squares.append(normalized)
                square_dict[normalized] = normalized in stops
            elif mouse_pressed[2] and normalized in square_dict:
                print(f"Del {normalized}")
                squares.remove(normalized)
                del square_dict[normalized]

        window.fill((255, 255, 255))
        window.blit(SCALED_MAP, (0, 0))

        for squares, square_dict, color in lines_storage.values():
            for x, y in squares:
                color_square(x, y, color, dark=square_dict[(x, y)])

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
