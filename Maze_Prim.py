import pygame
import random

# Paramètres
WIDTH, HEIGHT = 1280, 720
GRID_SIZE = 100
CELL_SIZE = int(WIDTH / GRID_SIZE)

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recursive Division Maze Generation")

def enclose():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            if x == 0 or y == 0 or x == WIDTH - CELL_SIZE or y == HEIGHT - CELL_SIZE:
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
                pygame.display.update()

def add_wall(x, y):
    pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

def random_int(x_min, x_max):
    return random.randint(x_min, x_max)

def sub_recursive_division(x_min, y_min, x_max, y_max):
    if y_max - y_min > x_max - x_min:
        x = random_int(x_min + 1, x_max)
        y = random_int(y_min + 2, y_max - 1)

        if (x - x_min) % 2 == 0:
            x += 1 if random_int(0, 2) == 0 else -1

        if (y - y_min) % 2 == 1:
            y += 1 if random_int(0, 2) == 0 else -1

        for i in range(x_min + 1, x_max):
            if i != x:
                add_wall(i, y)

        if y - y_min > 2:
            sub_recursive_division(x_min, y_min, x_max, y)

        if y_max - y > 2:
            sub_recursive_division(x_min, y, x_max, y_max)

    else:
        x = random_int(x_min + 2, x_max - 1)
        y = random_int(y_min + 1, y_max)

        if (x - x_min) % 2 == 1:
            x += 1 if random_int(0, 2) == 0 else -1

        if (y - y_min) % 2 == 0:
            y += 1 if random_int(0, 2) == 0 else -1

        for i in range(y_min + 1, y_max):
            if i != y:
                add_wall(x, i)

        if x - x_min > 2:
            sub_recursive_division(x_min, y_min, x, y_max)

        if x_max - x > 2:
            sub_recursive_division(x, y_min, x_max, y_max)

def main():
    screen.fill(WHITE)
    enclose()
    sub_recursive_division(0, 0, int((WIDTH / CELL_SIZE)) - 1, int((HEIGHT / CELL_SIZE)) - 1)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()