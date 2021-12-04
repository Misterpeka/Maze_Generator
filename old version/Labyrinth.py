from tkinter import *

fenetre= Tk()

def alert():
    showinfo("alerte","Bravo!")

menubar= Menu(fenetre)

menu = Menu(menubar, tearoff=0)
menu.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu)
fenetre.config(menu=menubar)

canvas = Canvas(fenetre, width=600, height =600,background='blue')

canvas.pack()
