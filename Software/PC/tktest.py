"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
#from tkinter import *

#from ihm import *


    

"""
fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()

"""

valG = 1

def addPlot():
    global valG

    valG = valG+1
    ax.clear()
    ax.plot(range(10), [0, 0, 0, 0, 0, 8, 7, 1, 2, 3])
    print("ok")
    graph = FigureCanvasTkAgg(fig, master=nframe)
    canvas = graph.get_tk_widget()
  #  canvas.grid(row=0, column=0)


    

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
app = tk.Tk()
app.wm_title("Graphe Matplotlib dans Tkinter")

nframe= tk.Frame(app)

nframe.pack()

bouton_cliquer = tk.Button(app, text="Cliquez ici", fg="red",command=addPlot)
bouton_cliquer.pack(side="right")
 

fig = Figure(figsize=(10, 10), dpi=96)
ax = fig.add_subplot(111)
ax.plot(range(10), [5, 4, 2, 6, 9, 8, 7, 1, 2, 3])

 
graph = FigureCanvasTkAgg(fig, master=nframe)
canvas = graph.get_tk_widget()
canvas.grid(row=0, column=0)



app.mainloop()
