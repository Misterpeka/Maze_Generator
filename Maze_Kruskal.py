import pygame
import random
from collections import defaultdict

# Paramètres
WIDTH, HEIGHT = 1280, 720
GRID_SIZE = 100
CELL_SIZE = int(WIDTH / GRID_SIZE)

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kruskal Maze Generation")

def draw_cell(x, y, color):
    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

def get_neighbors(x, y, width, height):
    neighbors = []
    if x > 1:
        neighbors.append((x - 2, y))
    if x < width - 2:
        neighbors.append((x + 2, y))
    if y > 1:
        neighbors.append((x, y - 2))
    if y < height - 2:
        neighbors.append((x, y + 2))
    return neighbors

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, rank):
    x_root = find(x, parent)
    y_root = find(y, parent)

    if x_root == y_root:
        return False

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

    return True

def kruskal_maze_generation(width, height):
    screen.fill(WHITE)
    
    # Initialize the maze with walls
    for x in range(width):
        for y in range(height):
            if x % 2 == 0 or y % 2 == 0:
                draw_cell(x, y, BLACK)

    # Create edges and sets
    edges = []
    parent = {}
    rank = defaultdict(int)
    for x in range(1, width, 2):
        for y in range(1, height, 2):
            for nx, ny in get_neighbors(x, y, width, height):
                edges.append(((x, y), (nx, ny)))
            cell = (x, y)
            parent[cell] = cell

    # Shuffle edges
    random.shuffle(edges)

    # Kruskal's algorithm
    for edge in edges:
        cell1, cell2 = edge
        if union(cell1, cell2, parent, rank):
            cx = (cell1[0] + cell2[0]) // 2
            cy = (cell1[1] + cell2[1]) // 2
            draw_cell(cx, cy, WHITE)

    pygame.display.update()

def main():
    kruskal_maze_generation(int(WIDTH / CELL_SIZE), int(HEIGHT / CELL_SIZE))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
