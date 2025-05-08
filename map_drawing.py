import pygame

# README XD
# w skrócie możesz sobie rysować po mapie jak w paincie, koordynaty są zapisywane w pamięci
# klawisze: S - zapisz to co narysowałeś do pliku (tak, uwzględniłem to, że (0,0) jest w lewym dolnym rogu)
# D - usuń z mapy to co nabazgrałeś, F - zwiększ counter o 1 (nazwa pliku to "out_{counter}.txt")
# lewy myszki - rysuj w danym punkcie, prawy - wykasuj
# miłej zabawy

pygame.init()

clock = pygame.time.Clock()
MAP = pygame.image.load('494326145_622665457602355_2881458455950731912_n.png')
SIZE = MAP.get_size()
WINDOW_SIZE = SIZE[0] * 2, SIZE[1] * 2
WIDTH, HEIGHT = WINDOW_SIZE

SCALED_MAP = pygame.transform.scale(MAP, WINDOW_SIZE)

window = pygame.display.set_mode(WINDOW_SIZE)

SQUARE_SIZE = WIDTH // 100
PANEL_SIZE = WIDTH // 4

def color_square(x, y):
    rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(window, (255, 0, 0), rect)

def save(coords, filename="out.txt"):
    with open(filename, "w") as f:
        for x, y in coords:
            y = HEIGHT // SQUARE_SIZE - y
            f.write(f"({x},{y}),\n")

def main():
    run = True

    squares = []
    file_idx = 0
    filename = f"out_{file_idx}.txt"
    smooth_coloring = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not smooth_coloring:
                    x, y = pygame.mouse.get_pos()
                    normalized = x // SQUARE_SIZE, y // SQUARE_SIZE
                    if event.button == pygame.BUTTON_LEFT:
                        if normalized in squares:
                            print(f"Del {normalized}")
                            squares.remove(normalized)
                        else:
                            print(f"Add {normalized}")
                            squares.append(normalized)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_s:
                        save(squares, filename)
                        print('Coordinates saved')
                    case pygame.K_d:
                        squares.clear()
                        print('Coordinates purged')
                    case pygame.K_f:
                        file_idx += 1
                        filename = f"out_{file_idx}.txt"
                        print("File name changed to " + filename)
                    case pygame.K_SPACE:
                        smooth_coloring = not smooth_coloring


        if smooth_coloring:
            x, y = pygame.mouse.get_pos()
            normalized = x // SQUARE_SIZE, y // SQUARE_SIZE
            mouse_pressed = pygame.mouse.get_pressed()

            if mouse_pressed[0] and normalized not in squares:
                print(f"Add {normalized}")
                squares.append(normalized)
            elif mouse_pressed[2] and normalized in squares:
                print(f"Del {normalized}")
                squares.remove(normalized)

        window.fill((255, 255, 255))
        window.blit(SCALED_MAP, (0, 0))

        for x, y in squares:
            color_square(x, y)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
