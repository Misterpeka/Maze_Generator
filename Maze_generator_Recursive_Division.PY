from tkinter import *
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
            case[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), fill="white")
    #placer les pixels et créer le labyrinthe
    init_pixel()
    create_maze(maze_size)
    draw()
    print("FINI")


def init_pixel(): #placer les pixels
    for x in range(maze_size):
        for y in range(maze_size):
            pixel[x][y] = True
    for x in range(maze_size):
        pixel[x][0] = "WALL"
        pixel[0][x] = "WALL"
        pixel[x][maze_size-1] = "WALL"
        pixel[maze_size-1][x] = "WALL"

def create_maze(size): #Recurisve division
    x = round(size // 2)
    y = round(size // 2)
    for i in range(size):
        pixel[x][i] = False
        pixel[i][y] = False
        draw()
    create_way(x,y,size)
    draw()
    create_maze(size//2)
        
def create_way(x,y,size):
    k = random.randint(1,size-1)
    j = random.randint(1,size-1)
    pixel[x][k] = True
    pixel[j][y] = True

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
    create_maze(maze_size)
    complexe()
    print("FINI")

def rgb(rgb):
    return "#%02x%02x%02x" % rgb
    
# Lancement du programme
fenetre = Tk()
fenetre.title("Labyrinth")
fenetre.iconbitmap('Favicon.ico')
canvas = Canvas(fenetre, width=cote*maze_size, height=cote*maze_size, highlightthickness=0)
fenetre.minsize(cote*maze_size,cote*maze_size)
fenetre.maxsize(cote*maze_size,cote*maze_size)

def quit():
    fenetre.destroy()

menubar= Menu(fenetre)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Relancer", command=replay)
menu.add_separator()
menu.add_command(label="Quitter", command=quit)
menubar.add_cascade(label="Action", menu=menu)
fenetre.config(menu=menubar)

canvas.pack()

if __name__ == '__main__':
    main()
    fenetre.mainloop()