from tkinter import *
import random

maze_size = 35  # taille du labyrinth
cote = 25  # coté d'une cellule

nb=0

# Créer les matrices
case = [[0 for lig in range(maze_size)] for col in range(maze_size)]
pixel = [[ 0  for lig in range(maze_size)] for col in range(maze_size)]
# Calculer et dessiner le prochain tableau
def tableau():
    dessiner()

# Données initiales
def init():
    for y in range(maze_size):
        for x in range(maze_size):
            case[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), fill="white")
    #placer les pixels
    init_pixel()

def init_pixel(): #placer les pixels
    nb = 0 
    for i in range(maze_size):
        pixel[0][i] = -1
        for j in range(1,maze_size):
            if j % 2 == 0:
                pixel[j][i] = -1
            elif i % 2 == 1:
                pixel[j][i] = 0
            else:
                pixel[j][i] = -1
        for x in range(maze_size):
            for y in range(maze_size):
                if pixel[x][y] == 0:
                    nb += 1
                    pixel[x][y]= nb
    print(pixel)

def create_maze():
    x = random.randint(1,maze_size-1)
    print("X=",x)
    y= 0
    if x % 2 == 0: 
        y = random.randint(1,((maze_size-1)/2)*2)
        print("y-1=",y)
    else:
        y = random.randint(2,((maze_size-2)/2)*2)
        print("y-2=",y)

    cell_1=0
    cell_2=0
    if pixel[x-1][y]==-1:
        cell_1= pixel[x][y-1]
        print("cell1-1=",cell_1)
        cell_2=pixel[x][y+1]
        print("Cell2-1=",cell_2)
    else:
        cell_1= pixel[x-1][y]
        print("cell1=",cell_1)
        cell_2= pixel [x+1][y]
        print("Cell2=",cell_2)
                    
    if cell_1 != cell_2:
        case[x][y] = 0
        canvas.itemconfig(case[x][y], fill='white')
    for i in range(1,maze_size-1,2):
        for j in range(1,maze_size-1,2):
            if pixel[i][j] == cell_2:
                pixel[i][j] = cell_1


    pixel[0][1]  = 0 
    pixel[maze_size-1][maze_size-2] = 0
    
def is_finished():
    for ligne in pixel:
        for colonne in ligne:
            if colonne > 0 : 
                return 1
    return 0


# Dessiner tous les pixels
def rgb(rgb):
    return "#%02x%02x%02x" % rgb

def dessiner():
    for y in range(maze_size):
        for x in range(maze_size):
            if pixel[x][y]==0:
                coul = "white"
            elif pixel[x][y] > 0:
                coul= rgb((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            elif pixel[x][y]==-1:
                coul = "black"
            canvas.itemconfig(case[x][y], fill=coul)
                
        
# Lancement du programme
fenetre = Tk()
fenetre.title("Labyrinth")
canvas = Canvas(fenetre, width=cote*maze_size, height=cote*maze_size, highlightthickness=0)
fenetre.minsize(maze_size*cote,maze_size*cote)
fenetre.maxsize(maze_size*cote,maze_size*cote)
canvas.pack()
init()
create_maze()
tableau()
fenetre.mainloop()