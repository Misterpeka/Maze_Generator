from tkinter import *
import random

haut = 50
larg = 100  # taille du labyrinth
cote = 10  # coté d'une cellule
vaccinated_percentage = 0 
time_before_death = 0 
time_before_cure = 0 
nb_sick = 1
contagious_level = 0 


# Créer les matrices
case = [[0 for lig in range(haut)] for col in range(larg)]
pixel = [[ 0  for lig in range(haut)] for col in range(larg)]
def tableau():
    dessiner()
    #fenetre.after(1, tableau)

def init():
    for y in range(haut):
        for x in range(larg):
            case[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), fill="white")
    #placer les pixels et créer le labyrinthe
    init_pixel()
    for i in range(nb_sick):
        set_random_malade()

def init_pixel():
    Placer = ["ALIVE","VACCINER"]
    for x in range(larg):
        for y in range(haut):
            pixel[x][y]= random.choice(Placer)

def set_random_malade():
    x = random.randint(0,larg)
    y = random.randint(0,haut)
    pixel[x][y] = "MALADE"

def check()
    x = random.randint(0,larg)
    y = random.randint(0,haut)
    if pixel[x][y] = "MALADE":
        check()
    else:
        if pixel[x+1][y] = "MALADE":
            return True

        elif pixel[x-1][y] = "MALADE":
        elif pixel[x][y-1] = "MALADE":
        elif pixel[x][y+1] = "MALADE":
        elif pixel[x-1][y+1] = "MALADE":
        elif pixel[x+1][y-1] = "MALADE":
        elif pixel[x-1][y-1] = "MALADE":
        elif pixel[x+1][y+1] = "MALADE":

def rgb(rgb):
    return "#%02x%02x%02x" % rgb
    
def dessiner():
    for y in range(haut):
        for x in range(larg):
            if pixel[x][y] == "ALIVE":
                coul = rgb((0,255,0))
            elif pixel[x][y] == "VACCINER":
                coul = rgb((0,0,255))
            elif pixel[x][y] == "MORT":
                coul = rgb((0,0,0))
            elif pixel[x][y] == "MALADE":
                coul = rgb((255,0,0))
            canvas.itemconfig(case[x][y], fill=coul)
fenetre = Tk()
fenetre.title("Jeu de la Vie")
canvas = Canvas(fenetre, width=cote*larg, height=cote*haut, highlightthickness=0)
fenetre.minsize(cote*larg,cote*haut)
fenetre.maxsize(cote*larg,cote*haut)
canvas.pack()
init()
tableau()
fenetre.mainloop()