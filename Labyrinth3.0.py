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
    complexe()
    print("FINI")
    replay()


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
    pixel[maze_size-1][maze_size-2] = True
    pixel[maze_size-2][maze_size-2] = True
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
        draw()
    pixel[0][1] = True #départ

def check(x,y): #regarder les cases autour
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

def complexe(): #rends le labyrinthe complexe
    for i in range(maze_size):
        x = random.randint(1,maze_size-1)
        y = random.randint(1,maze_size-1)
        if pixel[x][y] == False: 
            if pixel[x][y+1] == False and pixel[x][y-1] == False and pixel[x-1][y] == True and pixel[x+1][y] == True:
                pixel[x][y] = True
                draw()
            if pixel[x-1][y] == False and pixel[x-1][y] == False and pixel[x][y-1] == True and pixel[x][y+1] == True:
                pixel[x][y] = True
                draw()

def draw(): #affiche le labyrinthe
    fenetre.update()
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

    canvas.itemconfig(case[0][1], fill=rgb((0,255,0))) #départ
    canvas.itemconfig(case[maze_size-1][maze_size-2], fill=rgb((255,0,0))) #arrivé

def replay():
    init_pixel()
    create_maze()
    complexe()
    print("FINI")

def rgb(rgb):
    return "#%02x%02x%02x" % rgb
# Lancement du programme
fenetre = Tk()
fenetre.title("Labyrinth")
canvas = Canvas(fenetre, width=cote*maze_size, height=cote*maze_size, highlightthickness=0)
fenetre.minsize(cote*maze_size,cote*maze_size)
fenetre.maxsize(cote*maze_size,cote*maze_size)
canvas.pack()

if __name__ == '__main__':
    main()
    fenetre.mainloop()