import tkinter as tk

HEIGHT = 500
WIDTH = 500
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()


def draw_pixel(event):
    """un pixel de couleur rouge s'affiche à l'endroit où l'on a cliqué"""
    #canvas.create_rectangle(event.x - 1, event.y - 1, event.x + 1, event.y + 1, fill='red')
    canvas.create_line(event.x, event.y, event.x + 1, event.y, fill='red')

racine.bind("<Button-1>", draw_pixel)

racine.mainloop()

#https://www.python-course.eu/tkinter_events_binds.php  (lien pour bind)