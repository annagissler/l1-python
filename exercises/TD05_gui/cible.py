#mon programme
#import tkinter as tk

#HEIGHT = 600
#racine = tk.Tk()
#canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
#canvas.grid()

# tracé un cercle de centre r et de rayon (x,y)
# canvas.create_oval(x-r, y - r, x + y, y - r, fill=couleur)

#liste_couleurs=["blue", "green", "black", "yellow", "magenta", "red"]
#i = 300
#while i > 0:
    #j = i % 6
    #canvas.create_oval(300 - i, 300 - i, 300 + i, 300 + i, fill=liste_couleurs[j])
    #i -= 17


#racine.mainloop()

#correction

import tkinter as tk

COTE = 500
colors=["blue", "green", "black", "yellow", "magenta", "red"]
nb_cercles = 30

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=COTE, width=COTE)
canvas.grid()

epaisseur = (COTE // 2) // nb_cercles

for i in range(nb_cercles):
    canvas.create_oval((epaisseur * i, epaisseur * i),(COTE - epaisseur * i, COTE - epaisseur * i), fill=colors[i % len(colors)], outline=colors[i % len(colors)])

racine.mainloop()
