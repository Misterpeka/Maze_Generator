from tkinter import *
import random

maze_size = 35  # taille du labyrinth
cote = 25  # coté d'une cellule

# Créer les matrices
case = [[0 for lig in range(maze_size)] for col in range(maze_size)]
pixel = [["WALL" for lig in range(maze_size)] for col in range(maze_size)]

# Données initiales
def main():
    for y in range(maze_size):
        for x in range(maze_size):
            case[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), fill="white")
    
    create_maze(0, 0, maze_size - 1, maze_size - 1)

    draw()
    print("FINI")

def create_maze(x1, y1, x2, y2):
    if x2 - x1 < 2 or y2 - y1 < 2:
        return

    hx = random.randrange(x1 + 1, x2, 2) if x2 - x1 > 2 else x1 + 1
    vy = random.randrange(y1 + 1, y2, 2) if y2 - y1 > 2 else y1 + 1

    for x in range(x1 + 1, x2, 2):
        pixel[x][vy] = "WALL"
    for y in range(y1 + 1, y2, 2):
        pixel[hx][y] = "WALL"

    door_positions = [
        (hx, random.randrange(y1 + 1, vy, 2) if vy - y1 > 2 else y1 + 1),
        (hx, random.randrange(vy + 1, y2, 2) if y2 - vy > 2 else vy + 1),
        (random.randrange(x1 + 1, hx, 2) if hx - x1 > 2 else x1 + 1, vy),
        (random.randrange(hx + 1, x2, 2) if x2 - hx > 2 else hx + 1, vy),
    ]
    random.shuffle(door_positions)
    for _ in range(3):
        door_x, door_y = door_positions.pop()
        pixel[door_x][door_y] = "PATH"

    create_maze(x1, y1, hx - 1, vy - 1)
    create_maze(hx + 1, y1, x2, vy - 1)
    create_maze(x1, vy + 1, hx - 1, y2)
    create_maze(hx + 1, vy + 1, x2, y2)


def draw(): #affiche le labyrinthe
    fenetre.update()
    for y in range(maze_size):
        for x in range(maze_size):
            if pixel[x][y] == "PATH":
                coul = "white"
                canvas.itemconfig(case[x][y], fill=coul)
            elif pixel[x][y] == "WALL":
                coul = "black"
                canvas.itemconfig(case[x][y], fill=coul)

    canvas.itemconfig(case[1][0], fill=rgb((0,255,0))) #départ
    canvas.itemconfig(case[maze_size-2][maze_size-1], fill=rgb((255,0,0))) #arrivé

def replay():
    global pixel
    pixel = [["WALL" for lig in range(maze_size)] for col in range(maze_size)]
    create_maze(0, 0, maze_size - 1, maze_size - 1)
    draw()
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
