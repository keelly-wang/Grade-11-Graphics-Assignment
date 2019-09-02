from tkinter import *
from time import *
from random import*

myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="white")
s.pack()

#start pos
ball1x = randint(0,700)
ball1y = randint(0,700)
ball2x = randint(0,700)
ball2y = randint(0,700)
xInc1 = randint(-10,10)
yInc1 = randint(-10,10)
xInc2 = randint(-10,10)
yInc2 = randint(-10,10)
col1 = "green"
col2 = "yellow"
colourSame = False

while True:
    ball1 = s.create_oval(ball1x,ball1y,ball1x+100, ball1y+100, fill = col1)
    ball2 = s.create_oval(ball2x,ball2y,ball2x+100,ball2y+100, fill = col2)
    s.update()
    sleep(0.03)
    s.delete(ball1, ball2)
    
    #bounce
    if ball1x <= 0 or ball1x + 100 >= 800:
        xInc1 = -xInc1
    if ball1y <= 0 or ball1y + 100 >= 800:
        yInc1 = -yInc1
    if ball2x <= 0 or ball2x + 100 >= 800:
        xInc2 = -xInc2
    if ball2y <= 0 or ball2y + 100 >= 800:
        yInc2 = -yInc2

    #increment statements
    ball1x = ball1x + xInc1
    ball1y = ball1y + yInc1
    ball2x = ball2x + xInc2
    ball2y = ball2x + yInc2

    
    if ((ball1x-ball2x)**2+(ball1y-ball2y)**2)**(0.5) < 100 and colourSame == False:
        col2 = "red"
        col1 = "blue"
        colourSame = True

    

    
