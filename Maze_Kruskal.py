import pygame
import random
from collections import defaultdict, deque

# Paramètres
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
GRID_SIZE = 100
CELL_SIZE = int(min(WINDOW_WIDTH / GRID_SIZE, WINDOW_HEIGHT / GRID_SIZE))

GRID_WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
GRID_HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)

WIDTH = GRID_WIDTH * CELL_SIZE
HEIGHT = GRID_HEIGHT * CELL_SIZE

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)  # Ajout de la couleur bleu foncé

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kruskal Maze Generation and Solving")

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

def get_unblocked_neighbors(x, y, width, height, visited):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx] and not is_wall(nx, ny):
            neighbors.append((nx, ny))

    return neighbors

def is_wall(x, y):
    return screen.get_at((x * CELL_SIZE, y * CELL_SIZE)) == BLACK

def break_walls(num_walls_to_break, width, height):
    walls_broken = 0
    while walls_broken < num_walls_to_break:
        x, y = random.randint(1, width - 2), random.randint(1, height - 2)
        if is_wall(x, y) and len(get_neighbors(x, y, width, height)) > 1:
            draw_cell(x, y, WHITE)
            walls_broken += 1

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

    # Draw entrance and exit
    draw_cell(0, 1, GREEN)
    draw_cell(width - 1, height - 2, RED)

    pygame.display.update()

def gradient_color(distance, max_distance):
    blue_intensity = int((distance / max_distance) * 255)
    yellow_intensity = 255 - int((distance / max_distance) * 255)
    return (yellow_intensity, 0, blue_intensity)

def solve_maze(width, height):
    start = (0, 1)
    end = (width - 1, height - 2)
    visited = [[False for _ in range(width)] for _ in range(height)]
    distance = [[0 for _ in range(width)] for _ in range(height)]
    
    queue = deque()
    queue.append(end)
    visited[end[1]][end[0]] = True
    max_distance = 0

    while queue:
        x, y = queue.popleft()
        if (x, y) == start:
            break
        for nx, ny in get_unblocked_neighbors(x, y, width, height, visited):
            visited[ny][nx] = True
            distance[ny][nx] = distance[y][x] + 1
            max_distance = max(max_distance, distance[ny][nx])
            queue.append((nx, ny))
            draw_cell(nx, ny, DARK_BLUE)
            pygame.time.delay(1)
            pygame.display.update()

    x, y = start
    path = []
    while (x, y) != end:
        path.append((x, y))
        unblocked_neighbors = get_unblocked_neighbors(x, y, width, height, visited)
        if not unblocked_neighbors:
            break
        nx, ny = min(unblocked_neighbors, key=lambda p: distance[p[1]][p[0]])
        x, y = nx, ny

    path.append(end)

    # Dessiner le chemin le plus court en vert
    print(path)
    for x, y in path:
        draw_cell(x, y, GREEN)
        pygame.display.update()
        pygame.time.delay(5)

    draw_cell(end[0], end[1], RED)
    pygame.display.update()





def main():
    kruskal_maze_generation(GRID_WIDTH, GRID_HEIGHT)
    break_walls(50, GRID_WIDTH, GRID_HEIGHT)  # Casse 50 murs aléatoirement
    solve_maze(GRID_WIDTH, GRID_HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
