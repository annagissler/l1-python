import tkinter as tk
import random as rd

ma_couleur = "blue"
HEIGHT = 600
WIDTH = 600

racine = tk.Tk()
racine.title("Mon dessin")

objet=[]

def undo():
    if objet == []:
        pass
    else:
        if canvas.type(objet[-1]) == "line":
            #for i in range(1):
            canvas.delete(objet.pop())
            canvas.delete(objet.pop())
        else:
            canvas.delete(objet.pop())

#def undo():
    #repeat = 1
    #if len(objet) != 0:
        #if canvas.type(objet[-1]) == "line":
            #repeat = 2
        #for i in range(repeat):
            #canvas.delete(objets[-1])
            #del(objet[-1])

def choisir():
    """Demande une couleur à l'utilisateur dans le terminal"""
    global ma_couleur 
    ma_couleur = input("Choisis une couleur")
    print(objet)

    
def cercle():
    """cercle de diamètre 100 et de couleur bleu"""
    global objets #marche sans mais lorsqu'on change de version ou si on veut faire des calculs le programme peut afficher des erreurs
    #donc lorsqu'on change un valeur global toujours mettre global lorsque dans une fonction on la change
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    cercle = canvas.create_oval(x, y, x + 100, y + 100, fill=ma_couleur)
    objet.append(cercle)

def carre():
    """affiche un carré rouge de côté 100"""
    global objets
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    carre = canvas.create_rectangle(x, y, x + 100, y + 100, fill=ma_couleur)
    objet.append(carre)

def croix():
    """afficher une croix jaune inscrite dans un carré de côté 100"""
    global objets
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    croix = canvas.create_line(x, y, x + 100, y + 100, fill=ma_couleur)
    objet.append(croix)
    croix = canvas.create_line(x + 100, y, x, y + 100, fill=ma_couleur)
    objet.append(croix)



bouton1 = tk.Button(text="Choisir une couleur", command=choisir, font = ("helvetica", "20"), fg='red',padx=20, bd= 10)
bouton1.grid(row=0, column=1)

bouton2 = tk.Button(text="Cercle", command=cercle, font = ("helvetica", "30"), fg = 'blue', padx=20, bd=10)
bouton2.grid(row=1, column=0)

bouton3 = tk.Button(text="carré", command=carre, font = ("helvetica", "30"), fg = 'blue', padx=20).grid(row=2, column=0)

bouton4 = tk.Button(text="croix", command=croix, font = ("helvetica", "30"), fg = 'blue', padx=20, relief="raised")
bouton4.grid(row=3, column=0)

bouton5 = tk.Button(text="Undo", command=undo, font = ("helvetica", "20"), fg='red',padx=20, bd= 10)
bouton5.grid(row=0, column=2)

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH, relief="raised", bd=10)
canvas.grid(row=1, column=1, rowspan=3, columnspan=2)

racine.mainloop()
