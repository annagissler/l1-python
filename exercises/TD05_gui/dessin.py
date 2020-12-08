import tkinter as tk
import random as rd

ma_couleur = "blue"
HEIGHT = 600
WIDTH = 600

racine = tk.Tk()
racine.title("Mon dessin")

def choisir():
    """Demande une couleur à l'utilisateur dans le terminal"""
    global ma_couleur
    ma_couleur = input("Choisis une couleur")
    

def cercle():
    """cercle de diamètre 100 et de couleur bleu"""
    #x = rd.randint(0, 600)
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    canvas.create_oval(x, y, x + 100, y + 100, fill=ma_couleur)

def carre():
    """affiche un carré rouge de côté 100"""
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    canvas.create_rectangle(x, y, x + 100, y + 100, fill=ma_couleur)

def croix():
    """afficher une croix jaune inscrite dans un carré de côté 100"""
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    canvas.create_line(x, y, x + 100, y + 100, fill=ma_couleur)
    canvas.create_line(x + 100, y, x, y + 100, fill=ma_couleur)



bouton1 = tk.Button(text="Choisir une couleur", command=choisir, font = ("helvetica", "20"), fg='red',padx=20, bd= 10)
bouton1.grid(row=0, column=1)  

bouton2 = tk.Button(text="Cercle", command=cercle, font = ("helvetica", "30"), fg = 'blue', padx=20, bd=10)
bouton2.grid(row=1, column=0)

bouton3 = tk.Button(text="carré", command=carre, font = ("helvetica", "30"), fg = 'blue', padx=20).grid(row=2, column=0)

bouton4 = tk.Button(text="croix", command=croix, font = ("helvetica", "30"), fg = 'blue', padx=20, relief="raised")
bouton4.grid(row=3, column=0)

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH, relief="raised", bd=10)
canvas.grid(row=1, column=1, rowspan=3)

racine.mainloop()
