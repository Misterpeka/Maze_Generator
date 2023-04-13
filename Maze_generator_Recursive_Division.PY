import pygame
import random
import sys

maze_size = 35
cell_size = 25

walls_to_add = []  # Ajout de cette ligne
wall_creation_delay = 5  # Ajout de cette ligne



def init_maze():
    maze = [['PATH' for _ in range(maze_size)] for _ in range(maze_size)]  # Change WALL to PATH
    recursive_division(maze)
    return maze


def recursive_division(grid):
    enclose(grid)

    def sub_recursive_division(x_min, y_min, x_max, y_max):
        if y_max - y_min > x_max - x_min:
            x = random.randint(x_min + 1, x_max)
            y = random.randint(y_min + 2, y_max - 1)

            if (x - x_min) % 2 == 0:
                x += 1 if random.randint(0, 2) == 0 else -1

            if (y - y_min) % 2 == 1:
                y += 1 if random.randint(0, 2) == 0 else -1

            for i in range(x_min + 1, x_max):
                if i != x:
                    add_wall(grid, i, y)

            if y - y_min > 2:
                sub_recursive_division(x_min, y_min, x_max, y)

            if y_max - y > 2:
                sub_recursive_division(x_min, y, x_max, y_max)

        else:
            x = random.randint(x_min + 2, x_max - 1)
            y = random.randint(y_min + 1, y_max)

            if (x - x_min) % 2 == 1:
                x += 1 if random.randint(0, 2) == 0 else -1

            if (y - y_min) % 2 == 0:
                y += 1 if random.randint(0, 2) == 0 else -1

            for i in range(y_min + 1, y_max):
                if i != y:
                    add_wall(grid, x, i)

            if x - x_min > 2:
                sub_recursive_division(x_min, y_min, x, y_max)

            if x_max - x > 2:
                sub_recursive_division(x, y_min, x_max, y_max)

    sub_recursive_division(0, 0, len(grid) - 1, len(grid[0]) - 1)

def add_wall(grid, x, y):
    walls_to_add.append((x, y))  # Ajout de cette ligne

def enclose(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
                grid[i][j] = 'WALL'  # Change add_wall to direct assignment


def draw_maze(screen, maze):
    for y in range(maze_size):
        for x in range(maze_size):
            color = (0, 0, 0) if maze[x][y] == 'WALL' else (255, 255, 255)
            pygame.draw.rect(screen, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))

def main():
    pygame.init()
    screen = pygame.display.set_mode((cell_size * maze_size, cell_size * maze_size))
    pygame.display.set_caption("Recursive Division Maze")

    maze = init_maze()

    wall_creation_timer = 0  # Ajout de cette ligne

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Ajout de ce bloc de code
        if walls_to_add and wall_creation_timer <= 0:
            x, y = walls_to_add.pop(0)
            maze[x][y] = 'WALL'
            wall_creation_timer = wall_creation_delay
        else:
            wall_creation_timer -= 1

        draw_maze(screen, maze)
        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

