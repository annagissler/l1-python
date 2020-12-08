import tkinter as tk
import random as rd

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=256, width=256)
canvas.grid(row=1, column=1, rowspan=3)

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color):
    """colorie le pixel (i, j) du canvas de la couleur color"""
    canvas.create_line(i, j, i+1, j, fill=color)


def ecran_aleatoire():
    for i in range(256):
        for j in range(256):
            couleur = get_color(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
            draw_pixel(i, j, couleur)


def degrade_2D():
    for i in range(256):
        for j in range(256):
            couleur = get_color(i, 0, j)
            draw_pixel(i, j, couleur)

def degrade_gris():
    for i in range(256):
        couleur = get_color(i, i, i)
        for j in range(256):
            draw_pixel(i, j, couleur)


bouton1 = tk.Button(text="ALéatoire", command=ecran_aleatoire, font = ("helvetica", "20"), fg='blue')
bouton1.grid(row=1, column=0)  

bouton2 = tk.Button(text="Dégradé gris", command=degrade_gris, font = ("helvetica", "20"), fg='blue')
bouton2.grid(row=2, column=0)  

bouton3 = tk.Button(text="Dégradé 2D", command=degrade_2D, font = ("helvetica", "20"), fg='blue')
bouton3.grid(row=3, column=0)


racine.mainloop()
