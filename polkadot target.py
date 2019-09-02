from tkinter import*
from random import*

master = Tk()

s = Canvas(master, width=600, height=600)
s.pack()

for n in range(10000):
    x = randint(0,600)
    y = randint(0,600)
    if ((x-300)**2+(y-300)**2)**0.5 <= 100:
        s.create_oval(x-2,y-2,x+2,y+2, outline = "red", fill = "red")
    elif ((x-300)**2+(y-300)**2)**0.5 <= 200:
        s.create_oval(x-2,y-2,x+2,y+2, outline = "blue", fill = "blue")
    elif ((x-300)**2+(y-300)**2)**0.5 <= 300:
        s.create_oval(x-2,y-2,x+2,y+2, outline = "green", fill = "green")
    else:
        s.create_oval(x-2,y-2,x+2,y+2, fill = "black")

s.update()
