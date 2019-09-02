from tkinter import *

myInterface = Tk()
s = Canvas(myInterface, width=1000, height=800, background="yellow")
s.pack()

rows = int(input("how many rows do you want your fraction wall to have? " ))
brickHeight = 800/rows
for i in range(1,rows+1):
    s.create_line(0,brickHeight*i, 1000, brickHeight*i, fill = "purple")
    brickWidth = 1000/i
    for n in range(i):
        s.create_line(brickWidth*n,brickHeight*(i-1),brickWidth*n,brickHeight*i,fill = "purple")
s.update()
