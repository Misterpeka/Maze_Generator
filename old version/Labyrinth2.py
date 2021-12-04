from tkinter import *
import random

maze_size = 35  # taille du labyrinth
cote = 25  # coté d'une cellule
case_noir = 1
case_blanc = 0

# Créer les matrices
case = [[0 for row in range(maze_size)] for col in range(maze_size)]
pixel = [[case_blanc for row in range(maze_size)] for col in range(maze_size)]

# Calculer et dessiner le prochain tableau
def tableau():
    dessiner()
    fenetre.after(100, tableau)

# Données initiales
def init():
    for y in range(maze_size):
        for x in range(maze_size):
            case[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), fill="white")
    #placer les pixels
    init_pixel()

def init_pixel(): #placer les pixels
    for i in range(maze_size):
        pixel[0][i] = case_noir
        j=1
        for j in range(1,maze_size):
            if j % 2 == 0:
                pixel[j][i] = case_noir
            elif i % 2 == 1:
                pixel[j][i] = case_blanc
            else:
                pixel[j][i] = case_noir
        for i in range(0,maze_size-1):
            if pixel[j][i] == 0:
                pixel[j][i] = random.randint(2,10)
        
    pixel[0][1]=case_blanc
    pixel[maze_size-1][maze_size-2]=case_blanc
# Dessiner toutes les cellules
def dessiner():
    for y in range(maze_size):
        for x in range(maze_size):
            if pixel[x][y]==0:
                coul = "white"
            elif pixel[x][y] < 2:
                coul= "red"
            else:
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
tableau()
fenetre.mainloop()
