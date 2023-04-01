import pygame
import random
import sys

maze_size = 35  # taille du labyrinth
cote = 25  # coté d'une cellule

# Créer les matrices
case = [[0 for lig in range(maze_size)] for col in range(maze_size)]
pixel = [[ 0  for lig in range(maze_size)] for col in range(maze_size)]

# Données initiales
def main():
    for y in range(maze_size):
        for x in range(maze_size):
            case[x][y] = pygame.Rect(x * cote, y * cote, cote, cote)
    # placer les pixels et créer le labyrinthe
    init_pixel()
    create_maze()
    complexe()
    path = find_shortest_path((0, 1), (maze_size - 1, maze_size - 2))
    draw_path(path)
    print("FINI")

def init_pixel(): # placer les pixels
    for x in range(maze_size):
        pixel[x][0] = "WALL"
        pixel[x][maze_size-1] = "WALL"
        pixel[0][x] = "WALL"
        pixel[maze_size-1][x] = "WALL"
    for i in range(1,maze_size-1):
        for j in range(1,maze_size-1):
            pixel[i][j] = False

def create_maze(): # Exploration exhaustive / Depth-first search
    x = 0
    y = 1
    x_position=[]
    y_position=[]

    while x != maze_size-1 or y != maze_size-2:
        if len(check(x,y)) >= 1:
            Dir = random.choice(check(x,y))
        else:
            Dir = []
        if Dir == "EAST":
            pixel[x+2][y] = True
            pixel[x+1][y] = True
            x_position.append(x)
            y_position.append(y)
            x += 2
        elif Dir == "WEST":
            pixel[x-2][y] = True
            pixel[x-1][y] = True
            x_position.append(x)
            y_position.append(y)
            x -= 2
        elif Dir == "SOUTH":
            pixel[x][y+2] = True
            pixel[x][y+1] = True
            x_position.append(x)
            y_position.append(y)
            y += 2
        elif Dir == "NORTH":
            pixel[x][y-2] = True
            pixel[x][y-1] = True
            x_position.append(x)
            y_position.append(y)
            y -= 2
        if Dir == [] :
            x_position.reverse()
            y_position.reverse()
            if len(x_position) != 0 :
                x = x_position[0]
                y = y_position[0]

                x_position.pop(0)
                y_position.pop(0)
                x_position.reverse()
                y_position.reverse()
            else:
                x = maze_size-1
                y = maze_size-2
                pixel[maze_size-2][maze_size-2] = True

        draw()
    pixel[0][1] = True #départ
    pixel[maze_size-1][maze_size-2] = True

def check(x,y): # regarder les cases autour
    Direction_possible = []
    if x+2 <= maze_size-1:
        if pixel[x+2][y] == False:
            Direction_possible.append("EAST")
    if x-2 >= 0:
        if pixel[x-2][y] == False:
            Direction_possible.append("WEST")
    if y+2 <= maze_size-1:
        if pixel[x][y+2] == False:
            Direction_possible.append("SOUTH")
    if y-2 >= 0:
        if pixel[x][y-2] == False:
            Direction_possible.append("NORTH")
    return Direction_possible

def complexe(): # rends le labyrinthe complexe en cassant des murs au hasard 
    for i in range(maze_size):
        x = random.randint(1, maze_size-1)
        y = random.randint(1, maze_size-1)
        if pixel[x][y] == False: 
            if pixel[x][y+1] == False and pixel[x][y-1] == False and pixel[x-1][y] == True and pixel[x+1][y] == True:
                pixel[x][y] = True
                draw()
            if pixel[x-1][y] == False and pixel[x-1][y] == False and pixel[x][y-1] == True and pixel[x][y+1] == True:
                pixel[x][y] = True
                draw()

def check_chemin(x,y): # regarder les cases autour pour chemin
    Direction_possible = []
    if x+1 <= maze_size-1:
        if pixel[x+1][y] == False:
            Direction_possible.append("E")
    if x-1 >= 0:
        if pixel[x-1][y] == False:
            Direction_possible.append("W")
    if y+1 <= maze_size-1:
        if pixel[x][y+1] == False:
            Direction_possible.append("S")
    if y-1 >= 0:
        if pixel[x][y-1] == False:
            Direction_possible.append("N")
    return Direction_possible

def find_shortest_path(start, end): # TROUVER LE CHEMIN LE PLUS COURT
    distance = [[float('inf')] * maze_size for _ in range(maze_size)]
    distance[end[0]][end[1]] = 0

    queue = [end]
    visited = set()

    max_distance = 0

    while queue:
        x, y = queue.pop(0)

        if (x, y) == start:
            break

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < maze_size and 0 <= ny < maze_size and pixel[nx][ny] != "WALL" and pixel[nx][ny] != False:
                    if distance[nx][ny] > distance[x][y] + 1:
                        distance[nx][ny] = distance[x][y] + 1
                        max_distance = max(max_distance, distance[nx][ny])
                        queue.append((nx, ny))

    return distance, max_distance

def draw_path(path):  # affiche le chemin le plus court
    distance, max_distance = path
    for y in range(maze_size):
        for x in range(maze_size):
            if distance[x][y] != float('inf'):
                color = lerp_color((0, 255, 0), (0, 0, 255), distance[x][y] / max_distance)
                screen.fill(color, (x * cote, y * cote, cote, cote))
                pygame.display.update()
                pygame.time.delay(5)  # ajustez cette valeur pour changer la vitesse de l'animation


def lerp_color(color1, color2, t):
    r = int(color1[0] * (1 - t) + color2[0] * t)
    g = int(color1[1] * (1 - t) + color2[1] * t)
    b = int(color1[2] * (1 - t) + color2[2] * t)
    return (r, g, b)

def draw(): #affiche le labyrinthe
    for y in range(maze_size):
        for x in range(maze_size):
            if pixel[x][y] == True:
                coul = (255, 255, 255)
            elif pixel[x][y] == False:
                coul = (0, 0, 0)
            elif pixel[x][y] == "WALL":
                coul = (0, 0, 0)
            screen.fill(coul, (x * cote, y * cote, cote, cote))

    screen.fill((0, 255, 0), (0 * cote, 1 * cote, cote, cote)) #départ
    screen.fill((255, 0, 0), ((maze_size - 1) * cote, (maze_size - 2) * cote, cote, cote)) #arrivé
    pygame.display.update()

def replay():
    init_pixel()
    create_maze()
    complexe()
    print("FINI")

def quit_game():
    pygame.quit()
    sys.exit()

# Lancement du programme
pygame.init()
screen = pygame.display.set_mode((cote * maze_size, cote * maze_size))
pygame.display.set_caption("Labyrinth")
pygame.display.set_mode((cote * maze_size, cote * maze_size))

if __name__ == '__main__':
    main()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    replay()
                elif event.key == pygame.K_q:
                    quit_game()
            elif event.type == pygame.QUIT:
                quit_game()


