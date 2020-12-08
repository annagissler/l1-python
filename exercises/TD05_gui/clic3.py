import tkinter as tk

HEIGHT = 500
WIDTH = 500
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()

canvas.create_line((WIDTH/2, 0), (WIDTH/2, HEIGHT), fill='white') 

nb_clics = 0
point = (0,0)

def draw_line(event):
    global nb_clics, point
    if nb_clics == 0: #première fois on l'on clique
        nb_clics = 1
        point = (event.x, event.y)
    else:
        nb_clics = 0
        if (250 - event.x) * (250 - point[0]) >= 0: #du meme cote
            couleur = "blue"
        else:
            couleur = "red"
        canvas.create_line(point, event.x, event.y, fill=couleur)

racine.bind('<Button-1>', draw_line)
racine.mainloop()
