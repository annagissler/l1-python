import tkinter as tk

HEIGHT = 500
WIDTH = 500
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()

cpt = 0

def alterne(event):
    global cpt
    if cpt % 2 == 0:
        couleur = "white"
    else:
        couleur = "black"
    cpt += 1
    canvas.itemconfigure(rectangle, fill=couleur)
    if cpt > 9:
        racine.destroy()

        
rectangle = canvas.create_rectangle(100, 100, 400, 400, outline = "white", fill="black")
canvas.bind ("<Button-1>", alterne)
racine.mainloop()