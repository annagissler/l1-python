import tkinter as tk

HEIGHT = 500
WIDTH = 500
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()

cpt = 0
cercles = []

def dix_cercles(event):
    global cpt, cercles
    if cpt < 8:
        c = canvas.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, fill="red")
        cercles.append(c)
    elif cpt == 8:
       for c in cercles:
           canvas.itemconfigure(c, fill = "yellow")
    else:
        for c in cercles:
            canvas.delete(c)
        cercles = []
    cpt += 1
        
canvas.bind ("<Button-1>", dix_cercles)
racine.mainloop()