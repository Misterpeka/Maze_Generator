from tkinter import*
import os

def laby1():
    os.startfile("./Maze_Generator.py")

fenetre = Tk()
fenetre.title("Labyrinth")
fenetre.iconbitmap('Favicon.ico')
fenetre.minsize(500,500)
fenetre.maxsize(500,500)
canvas = Canvas(fenetre, width=500, height=500, highlightthickness=0)
bouton=Button(fenetre, text="LABY 1", command=laby1)
bouton.pack(side=LEFT, padx=5, pady=5)
fenetre.mainloop()