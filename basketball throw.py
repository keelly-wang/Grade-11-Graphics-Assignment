from tkinter import*
from time import*
master = Tk()

s = Canvas(master, width=1200, height=800)
s.pack()

#sky
r = 220
g = 237
b = 242
w = 550
for x in range(50):
    bkg = '#%02x%02x%02x' % (r, g, b)
    s.create_rectangle(0,0,1200,w, fill = bkg, outline = bkg)
    r = r-2
    g = g-1
    w = w-20

#bushes
for i in range(10):
    s.create_oval(i*130-100,500,i*130+100,700, fill = "#388429", outline = "#388429")

s.create_line(0,400,1200,400, width = 10, fill = "grey")
for x in range(-2,25):
    s.create_line(x*50,400,(x+3)*50,700, width = 10, fill = "grey")
    s.create_line(x*50,700,(x+3)*50,400, width = 10, fill = "grey")

s.create_rectangle(0,675,1200,800,fill = "#b47e2b", outline = "#b47e2b")

#NET
s.create_line(1100,350,1100,750, fill = "#754419", width = 20)
s.create_oval(1025,385,1095,415, outline = "black", width = 5)
hoop = s.create_line(1025,400,1025,415,1095,415,1095,400, smooth = True, width = 5)

###GRIDLINES
##spacing = 50
##for x in range(0, 1200, spacing): 
##    s.create_line(x, 25, x, 1000, fill="black")
##    s.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "black")
##
##for y in range(0, 1000, spacing):
##    s.create_line(25, y, 1200, y, fill="black")
##    s.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "black")

#INPUTS 
humanX = int(input("where do I shoot from? Enter an x-coordinate between 0 and 800 "))
while humanX < 0 or humanX > 800:
    humanX = int(input("there are a great many things I can do. I, however, cannot throw from beyond this virtual screen I reside in, or from behind the hoop. So please enter a value between 0 and 800: "))
humanY = 540
legN = [humanX+5, humanY+85, humanX+35, humanY+87, humanX+65, humanY+120, humanX+35, humanY+180, humanX+5, humanY+175, humanX+25, humanY+135, humanX-12, humanY+110]
bodyN = [humanX-15, humanY+40, humanX+10, humanY+5, humanX+60, humanY+15, humanX+40, humanY+60, humanX+40, humanY+100, humanX-20, humanY+110]
headN = [humanX+10,humanY-30]
armN = [humanX+35, humanY+35, humanX+63, humanY+59, humanX+92, humanY+35, humanX+97, humanY+50, humanX+63, humanY+80, humanX+22, humanY+60, humanX+20, humanY+40]
footN = [humanX+5, humanY+170, humanX+35, humanY+180, humanX+50, humanY+205, humanX-5, humanY+185]

#CREATE SHOOTER
body = s.create_polygon(bodyN[0],bodyN[1],bodyN[2],bodyN[3],bodyN[4],bodyN[5],bodyN[6],bodyN[7],bodyN[8],bodyN[9],bodyN[10],bodyN[11], fill = "#c10a0a", outline = "#c10a0a") 
head = s.create_oval(headN[0],headN[1],headN[0]+60,headN[1]+60, fill = "#FFC692", outline = "#FFC692")
leg = s.create_polygon(legN[0],legN[1],legN[2],legN[3],legN[4],legN[5],legN[6],legN[7],legN[8],legN[9],legN[10],legN[11],legN[12],legN[13], fill = "black", outline = "black")
ball = s.create_oval((armN[6]+armN[8])/2-15,(armN[5]+armN[7])/2-25,(armN[6]+armN[8])/2+35,(armN[5]+armN[7])/2+25, fill = "red")
arm = s.create_polygon(armN[0],armN[1],armN[2],armN[3],armN[4],armN[5],armN[6],armN[7],armN[8],armN[9],armN[10],armN[11],armN[12],armN[13], fill = "#e5b283", outline = "#e5b283")
foot = s.create_polygon(footN[0],footN[1],footN[2],footN[3],footN[4],footN[5],footN[6],footN[7], fill = "#c10a0a", outline = "#c10a0a")
s.update()
sleep(2)

#FIRST MOTION
for f in range(20):
    s.update()
    sleep(0.015)
    s.delete(leg,body,head,arm,foot,ball)

    legN = [legN[0] + 0.35, legN[1] - 1, legN[2] + 0.25, legN[3] - 1.5, legN[4] - 0.5, legN[5] - 0.5, legN[6], legN[7], legN[8], legN[9], legN[10] - 0.25, legN[11] - 0.5, legN[12] + 0.35, legN[13] - 1.5]
    bodyN = [bodyN[0]+0.5, bodyN[1]-1, bodyN[2]+0.5, bodyN[3]-1.5, bodyN[4]+0.5, bodyN[5]-1.5, bodyN[6]+0.5, bodyN[7]-1, bodyN[8]+0.5, bodyN[9]-1, bodyN[10]+0.5, bodyN[11]-1]
    headN = [headN[0]+0.75,headN[1]-2]
    armN = [armN[0]+0.75, armN[1]-2, armN[2]+1, armN[3]-3, armN[4]+1, armN[5]-3, armN[6]+1.25, armN[7]-3, armN[8]+1, armN[9]-3, armN[10]+0.75, armN[11]-2, armN[12]+0.75, armN[13]-2]

    body = s.create_polygon(bodyN[0],bodyN[1],bodyN[2],bodyN[3],bodyN[4],bodyN[5],bodyN[6],bodyN[7],bodyN[8],bodyN[9],bodyN[10],bodyN[11], fill = "#c10a0a",outline = "#c10a0a") 
    head = s.create_oval(headN[0],headN[1],headN[0]+60,headN[1]+60, fill = "#FFC692", outline = "#FFC692")
    leg = s.create_polygon(legN[0],legN[1],legN[2],legN[3],legN[4],legN[5],legN[6],legN[7],legN[8],legN[9],legN[10],legN[11],legN[12],legN[13], fill = "black", outline = "black")
    ball = s.create_oval((armN[6]+armN[8])/2-15,(armN[5]+armN[7])/2-25,(armN[6]+armN[8])/2+35,(armN[5]+armN[7])/2+25, fill = "red")
    arm = s.create_polygon(armN[0],armN[1],armN[2],armN[3],armN[4],armN[5],armN[6],armN[7],armN[8],armN[9],armN[10],armN[11],armN[12],armN[13], fill = "#e5b283", outline = "#e5b283")
    foot = s.create_polygon(footN[0],footN[1],footN[2],footN[3],footN[4],footN[5],footN[6],footN[7], fill = "#c10a0a", outline = "#c10a0a")

#SECOND MOTION    
for f in range(35):
    s.update()
    sleep(0.001)
    s.delete(leg,body,head,arm,foot,ball)
    footN = [footN[0]+0.35,footN[1]-1,footN[2]+0.25,footN[3]-0.5,footN[4],footN[5],footN[6]+0.5,footN[7]-1]
    legN = [legN[0] + 1,legN[1] - 2,legN[2] + 1,legN[3] - 2,legN[4] + 0.25,legN[5] - 1,legN[6] + 0.25,legN[7] - 0.5,legN[8] + 0.35,legN[9] -1,legN[10] + 0.25,legN[11] - 1,legN[12] + 1,legN[13] - 2]

    #body increments
    bodyN =[bodyN[0]+1.35, bodyN[1]-1.65, bodyN[2]+1, bodyN[3]-2.6, bodyN[4]+1, bodyN[5]-2.6, bodyN[6]+1.1,bodyN[7]-2.6,bodyN[8]+0.75,bodyN[9]-2.6,bodyN[10]+0.75,bodyN[11]-2.6]

    #head increments
    headN = [headN[0]+1, headN[1]-2.65]

    #arm increments
    armN = [armN[0]+0.75,armN[1]-2.5,armN[2]+1.6,armN[3]-3.5,armN[4]+1.6,armN[5]-3.5,armN[6]+1.85,armN[7]-3.5,armN[8]+1.6,armN[9]-3.5,armN[10]+1.35,armN[11]-2.5,armN[12]+1.35,armN[13]-2.5]

    body = s.create_polygon(bodyN[0],bodyN[1],bodyN[2],bodyN[3],bodyN[4],bodyN[5],bodyN[6],bodyN[7],bodyN[8],bodyN[9],bodyN[10],bodyN[11], fill = "#c10a0a", outline = "#c10a0a") 
    head = s.create_oval(headN[0],headN[1],headN[0]+60,headN[1]+60, fill = "#FFC692", outline = "#FFC692")
    leg = s.create_polygon(legN[0],legN[1],legN[2],legN[3],legN[4],legN[5],legN[6],legN[7],legN[8],legN[9],legN[10],legN[11],legN[12],legN[13], fill = "black", outline = "black")
    ball = s.create_oval((armN[6]+armN[8])/2-15,(armN[5]+armN[7])/2-25,(armN[6]+armN[8])/2+35,(armN[5]+armN[7])/2+25, fill = "red")
    arm = s.create_polygon(armN[0],armN[1],armN[2],armN[3],armN[4],armN[5],armN[6],armN[7],armN[8],armN[9],armN[10],armN[11],armN[12],armN[13], fill = "#e5b283", outline = "#e5b283")
    foot = s.create_polygon(footN[0],footN[1],footN[2],footN[3],footN[4],footN[5],footN[6],footN[7], fill = "#c10a0a", outline = "#c10a0a")


#BASKETBALL
ballStartX = (armN[6]+armN[8])/2
ballStartY = 400
ballEndX = 1050
ballEndY = 400
ballVertexX = (1050+ballStartX)/2
ballVertexY = 200
a = (400-200)/(1050-ballVertexX)**2

f = 0
ballY = 100
hoop = s.create_line(1025,400,1025,415,1095,415,1095,400, smooth = True, width = 5)
while ballY < 800:
    s.delete(ball)
    ballX = f*12 + ballStartX
    ballY = a*(ballX-ballVertexX)**2+200
    ball = s.create_oval(ballX-15,ballY-25,ballX+35,ballY+25, fill = "red")
    if ballX < 200:
        arm = s.create_polygon(armN[0],armN[1],armN[2],armN[3],armN[4],armN[5],armN[6],armN[7],armN[8],armN[9],armN[10],armN[11],armN[12],armN[13], fill = "#e5b283", outline = "#e5b283")
    if ballX > 1000:
        hoop = s.create_line(1025,400,1025,415,1095,415,1095,400, smooth = True, width = 5)
    s.update()
    sleep(0.03)
    f = f+1
s.update()









