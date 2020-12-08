import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

racine = tk.Tk()

canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

y1= 100
y2 = CANVAS_WIDTH - 250
x = CANVAS_HEIGHT / 2
canvas.create_line(x, y1, x, y2)
canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50) #(250, 150), (350, 50)
canvas.create_oval(x - 50, y2 + 50, x + 50, y2 - 50) #(250, 350), (350, 250)
canvas.create_oval(x - 50, (y1 + y2) // 2 + 50, x + 50, (y1 + y2) // 2 - 50)

canvas.grid()
racine.mainloop()


#canvas.create_oval((x0, y0), (x1, y1))