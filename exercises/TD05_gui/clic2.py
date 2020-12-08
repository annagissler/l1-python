import tkinter as tk

HEIGHT = 500
WIDTH = 500
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()

canvas.create_line((WIDTH/2, 0), (WIDTH/2, HEIGHT), fill='white')

#def affichage(event):
    #if (event.x, event.y) < (WIDTH // 2, 0):
        #canvas.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, fill='blue')
    #elif (event.x, event.y) > (WIDTH // 2, 0):
        #canvas.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, fill='red')


#correction 
def draw_cercle(event):
    if event.x < 250:
        couleur = "blue"
    else:
        couleur = "red"
    canvas.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, fill=couleur)

racine.bind("<Button-1>", draw_cercle)

racine.mainloop()