import pygame
import storage
from copy import copy

pygame.init()

clock = pygame.time.Clock()
MAP = pygame.image.load('utils/katowice.png')
SIZE = MAP.get_size()

WINDOW_SIZE = SIZE[0], SIZE[1]
WIDTH, HEIGHT = WINDOW_SIZE

SCALED_MAP = pygame.transform.scale(MAP, WINDOW_SIZE)
window = pygame.display.set_mode(WINDOW_SIZE)

SQUARE_SIZE = WIDTH // 150

# Kolory
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
CYAN = 0, 255, 255
MAGENTA = 255, 0, 255
ORANGE = 255, 128, 0
VIOLET = 128, 0, 255
BROWN = 139, 69, 19
PINK = 255, 192, 203
LIME = 191, 255, 0
NAVY = 0, 0, 128
SKY_BLUE = 135, 206, 235

BLACK = 0, 0, 0  # Kolor przystanków

COLORS = [
    RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE, VIOLET,
    BROWN, PINK, LIME, NAVY, SKY_BLUE
]

def color_square(x, y, color):
    rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(window, color, rect)

def main():
    run = True
    temp = 0

    lines_storage = {}
    stops = set()
    file_idx = 0

    # Wczytanie linii ze storage, wraz z przystankami
    for line in storage.storage:
        squares = []
        for square, stop in line:
            squares.append(square)
            if stop:
                stops.add(square)
        color = COLORS[file_idx % len(COLORS)]
        lines_storage[file_idx] = squares, color
        file_idx += 1

    # Nowa linia rysowana przez użytkownika
    new_line = []
    new_color = COLORS[file_idx % len(COLORS)]

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        x, y = pygame.mouse.get_pos()
        normalized = x // SQUARE_SIZE, y // SQUARE_SIZE
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0] and normalized not in new_line:
            new_line.append(normalized)
            temp += 1
            print(f"{normalized}")
            if temp == 2:
                run = False

        window.fill((255, 255, 255))
        window.blit(SCALED_MAP, (0, 0))

        # Rysowanie linii z pliku
        for squares, color in lines_storage.values():
            for x, y in squares:
                if (x, y) in stops:
                    color_square(x, y, BLACK)  # przystanek
                else:
                    color_square(x, y, color)

        # Rysowanie nowej linii
        for x, y in new_line:
            color_square(x, y, new_color)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
