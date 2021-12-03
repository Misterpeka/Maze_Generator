from tkinter import *
import random

maze_size = 35  # taille du labyrinth
cote = 25  # coté d'une cellule

# Créer les matrices
case = [[0 for lig in range(maze_size)] for col in range(maze_size)]
pixel = [[ 0  for lig in range(maze_size)] for col in range(maze_size)]

# Données initiales
def main():
    for y in range(maze_size):
        for x in range(maze_size):
            case[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), fill="white")
    #placer les pixels et créer le labyrinthe
    init_pixel()
    create_maze()

def init_pixel(): #placer les pixels
    for x in range(maze_size):
        pixel[x][0] = "WALL"
        pixel[x][maze_size-1] = "WALL"
        pixel[0][x] = "WALL"
        pixel[maze_size-1][x] = "WALL"
    for i in range(1,maze_size-1):
        for j in range(1,maze_size-1):
            pixel[i][j] = False

def create_maze(): #Exploration exhaustive
    x = 0
    y = 1
    x_position=[]
    y_position=[]

    while x != maze_size-1 and y != maze_size-2:
        print(check(x,y))
        if len(check(x,y)) >= 1:
            Dir = random.choice(check(x,y))
        else:
            Dir = []
        if Dir == "EAST":
            print("EST")
            pixel[x+2][y] = True
            pixel[x+1][y] = True
            x_position.append(x)
            y_position.append(y)
            x += 2
        elif Dir == "WEST":
            print("West")
            pixel[x-2][y] = True
            pixel[x-1][y] = True
            x_position.append(x)
            y_position.append(y)
            x -= 2
        elif Dir == "SOUTH":
            print("South")
            pixel[x][y+2] = True
            pixel[x][y+1] = True
            x_position.append(x)
            y_position.append(y)
            y += 2
        elif Dir == "NORTH":
            print("North")
            pixel[x][y-2] = True
            pixel[x][y-1] = True
            x_position.append(x)
            y_position.append(y)
            y -= 2
        if Dir == [] :
            print("RIEN")
            x_position.reverse()
            y_position.reverse()

            x = x_position[0]
            y = y_position[0]

            x_position.pop(0)
            y_position.pop(0)
            x_position.reverse()
            y_position.reverse()

    pixel[0][1] = True
    pixel[maze_size-1][maze_size-2] = False

def check(x,y):
    Direction_possible = []
    if x+2 <= maze_size:
        if pixel[x+2][y] == False:
            Direction_possible.append("EAST")
    if x-2 >= 0:
        if pixel[x-2][y] == False:
            Direction_possible.append("WEST")
    if y+2 <= maze_size:
        if pixel[x][y+2] == False:
            Direction_possible.append("SOUTH")
    if y-2 >= 0:
        if pixel[x][y-2] == False:
            Direction_possible.append("NORTH")
    return Direction_possible


def dessiner():
    for y in range(maze_size):
        for x in range(maze_size):
            if pixel[x][y] == True:
                coul = "white"
                canvas.itemconfig(case[x][y], fill=coul)
            elif pixel[x][y] == False:
                coul = "black"
                canvas.itemconfig(case[x][y], fill=coul)
            elif pixel[x][y] == "WALL":
                coul = "black"
                canvas.itemconfig(case[x][y], fill=coul)


def score_boxes(pixel):
    print("scoreboxes")
    pixel[0][1] = 0

    for x in range(1,maze_size-1):
        for y in range(1,maze_size-1):
            if pixel[x][y] >= 0:
                pixel[x][y] = 0


    color = 1
    distance = 1
    pixel[maze_size - 1][maze_size - 2] = 1
    canvas.itemconfig(case[maze_size - 1][maze_size - 2], fill=rgb((255,255,0)))

    while pixel[1][1] == 0:
        temp = pixel
        distance += 1
        for i in range (0,maze_size - 2,-1):
            for j in range (0,maze_size - 2,-1):
                if pixel[i][j] == 0 : 
                    if pixel[i][j - 1]  > 0 or pixel[i][j + 1] > 0 or pixel[i - 1][j] >  0 or pixel[i + 1][j] > 0:
                        temp[i][j] = distance
                        color += 1
                        canvas.itemconfig(case[i][j], fill=rgb((color * 1.5,color * 1.5,color * 1.5)))
        pixel = temp

    maze_size[1][0] = distance + 20

    for i in range(0,maze_size):
        for j in range(0,maze_size):
            if pixel[i][j] == 0: 
                pixel[i][j] = distance + 1 
            if maze_size[i][j] == -1:
                maze_size[i][j] = distance + 10   


def maze_solver():
    print("maze_solver")
    x = 1 
    y = 1
    while x != maze_size - 2 or y != maze_size - 2:
        print("test")
        up = pixel[y-1][x]
        down = pixel[y+1][x]
        left = pixel[y][x-1]
        right = pixel[y][x+1]
        if up <= down and up <= left and up <= right:
            canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))
            y = y - 1
        elif down <= up and down <= left and down <= right:
            canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))
            y = y + 1
        elif left <= up and left <= down and left <= right:
            canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))
            x = x - 1
        elif right <= up and right <= down and right <= left:
            canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))
            x = x + 1
    canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))


# Lancement du programme
fenetre = Tk()
fenetre.title("Labyrinth")
canvas = Canvas(fenetre, width=cote*maze_size, height=cote*maze_size, highlightthickness=0)
fenetre.minsize(cote*maze_size,cote*maze_size)
fenetre.maxsize(cote*maze_size,cote*maze_size)
canvas.pack()
main()
dessiner()
fenetre.mainloop()