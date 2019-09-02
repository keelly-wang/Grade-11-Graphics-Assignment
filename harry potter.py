from tkinter import*
from time import*
from random import*
from math import*
master = Tk()
s = Canvas(master, width=1200, height=800, background = "#8abdf5")
s.pack()

#gradient sky
r = 138
g = 189
b = 245
w = 900
for x in range(50):
    bkg = "#"+hex(r)[2:]+hex(g)[2:]+hex(b)[2:]
    s.create_oval(900-w,150-w,900+w,150+w, fill = bkg, outline = bkg)
    r = r+2
    g = g+1
    w = w-20

#clouds (randomly generated)
for x in range(randint(5,10)):
    y = randint(0,700)
    s.create_line(0,y,randint(200,600),randint(y-100,y+100),randint(600,1000),randint(y-100,y+100),1220,randint(y-100,y+100), fill = "white", width = randint(5,30), smooth = True)

#mountains (randomly generated)
mountCol = ["#DFD27C","#9D9754","#B4A851","#6E7649","#DFD27C", "#B4A851", "#6E7649"]
mountLoc = [0,200,200*2,200*3,200*4,200*5,200*6]
mount = list(zip(mountCol,mountLoc))
shuffle(mount)
mountRad = []
for n in range(7):
    mountR = randint(200,400)
    mountRad.append(mountR)
    s.create_oval(mount[n][1]-mountR,850-mountR,mount[n][1]+mountR,850+mountR, fill = mount[n][0], outline = mount[n][0])

#Harry flying
hX = -100
hY = 300
bX = 3000
bY = 5000
while hX <= 700:
    hX= hX + 8
    hY= 150*sin(pi/500*(hX+100))+300
    bX = bX - 22
    bY = bY - 48
    
    handle = s.create_line(hX, hY, hX+104, hY-39, width = 5, fill = "#492510")
    broom = s.create_polygon(hX-31, hY+1, hX, hY, hX-21, hY+26, hX-68, hY+21, fill= "#664719")
    broomknot = s.create_oval(hX-10, hY-3, hX, hY+7, fill = "#492510", outline = "#492510")
    leg = s.create_polygon(hX+23, hY+7, hX+21, hY+17, hX+3, hY+24, hX+2, hY+16, hX+11, hY+12, hX+14, hY-1, fill = "#31170a")
    foot = s.create_polygon(hX+2, hY+16, hX+3, hY+24, hX-3, hY+25, hX-2, hY+35, hX-9, hY+34, hX-11, hY+19, fill = "#1b1304")
    undercoat = s.create_polygon(hX+63, hY-38, hX+60, hY-30, hX+27, hY+12, hX+4, hY-4, hX-6, hY-22, fill = "#84141c", outline = "#c5871b", width = 3)
    overcoatY = s.create_polygon(hX-18, hY-16, hX-20, hY-20, hX+44, hY-39, hX+66, hY-34, hX+30, hY-6, fill = "#c5871b")
    overcoat = s.create_polygon(hX-20, hY-20, hX+41, hY-43, hX+63, hY-38, hX+27, hY-10, fill = "#84141c")
    head = s.create_oval(hX+36, hY-82, hX+84, hY-36, fill = "#e6c198", outline = "#e6c198")
    hair = s.create_polygon(hX+39, hY-39, hX+32, hY-64, hX+44, hY-79, hX+61, hY-87, hX+77, hY-79, hX+84, hY-69, hX+54, hY-59, fill = "black")
    hand = s.create_oval(hX+71, hY-29, hX+82, hY-19, fill = "#e6c198", outline = "#e6c198")
    arm = s.create_polygon(hX+41, hY-33, hX+57, hY-28, hX+74, hY-29, hX+75, hY-11, hX+55, hY-8, hX+32, hY-15, fill = "#84141c")
    eye = s.create_oval(hX+69, hY-56, hX+73, hY-52, fill = "black")
    glasses = s.create_oval(hX+64, hY-61, hX+78, hY-47, outline = "black")
    scar = s.create_line(hX+75, hY-71, hX+80, hY-67, hX+77, hY-66, hX+82, hY-59, width = 2, fill = "#e69900")
    bludger = s.create_oval(bX-25,bY-25,bX+25,bY+25, fill = "brown", outline = "brown")
    
    s.update()
    sleep(0.01)
    s.delete(handle,broom,broomknot,leg,foot,undercoat,overcoatY,overcoat,head,hair,hand,arm,eye,glasses,scar,bludger)   

handle = s.create_line(hX, hY, hX+104, hY-39, width = 5, fill = "#492510")
broom = s.create_polygon(hX-31, hY+1, hX, hY, hX-21, hY+26, hX-68, hY+21, fill= "#664719")
broomknot = s.create_oval(hX-10, hY-3, hX, hY+7, fill = "#492510", outline = "#492510")
leg = s.create_polygon(hX+23, hY+7, hX+21, hY+17, hX+3, hY+24, hX+2, hY+16, hX+11, hY+12, hX+14, hY-1, fill = "#31170a")
foot = s.create_polygon(hX+2, hY+16, hX+3, hY+24, hX-3, hY+25, hX-2, hY+35, hX-9, hY+34, hX-11, hY+19, fill = "#1b1304")
undercoat = s.create_polygon(hX+63, hY-38, hX+60, hY-30, hX+27, hY+12, hX+4, hY-4, hX-6, hY-22, fill = "#84141c", outline = "#c5871b", width = 3)
overcoatY = s.create_polygon(hX-18, hY-16, hX-20, hY-20, hX+44, hY-39, hX+66, hY-34, hX+30, hY-6, fill = "#c5871b")
overcoat = s.create_polygon(hX-20, hY-20, hX+41, hY-43, hX+63, hY-38, hX+27, hY-10, fill = "#84141c")
head = s.create_oval(hX+36, hY-82, hX+84, hY-36, fill = "#e6c198", outline = "#e6c198")
hair = s.create_polygon(hX+39, hY-39, hX+32, hY-64, hX+44, hY-79, hX+61, hY-87, hX+77, hY-79, hX+84, hY-69, hX+54, hY-59, fill = "black")
hand = s.create_oval(hX+71, hY-29, hX+82, hY-19, fill = "#e6c198", outline = "#e6c198")
arm = s.create_polygon(hX+41, hY-33, hX+57, hY-28, hX+74, hY-29, hX+75, hY-11, hX+55, hY-8, hX+32, hY-15, fill = "#84141c")
eye = s.create_oval(hX+69, hY-56, hX+73, hY-52, fill = "black")
glasses = s.create_oval(hX+64, hY-61, hX+78, hY-47, outline = "black")
scar = s.create_line(hX+75, hY-71, hX+80, hY-67, hX+77, hY-66, hX+82, hY-59, width = 2, fill = "#e69900")
bludger = s.create_oval(bX-25,bY-25,bX+25,bY+25, fill = "brown", outline = "brown")

sleep(1)

#Harry falling
x = 0
for f in range(70):
    s.update()
    sleep(0.01)
    s.delete(handle,broom,broomknot,leg,foot,undercoat,overcoatY,overcoat,head,hair,hand,arm,eye,glasses,scar,bludger)
    hY = 0.25*x**2 + 160
    handle = s.create_line(hX, hY, hX+104, hY-39, width = 5, fill = "#492510")
    broom = s.create_polygon(hX-31, hY+1, hX, hY, hX-21, hY+26, hX-68, hY+21, fill= "#664719")
    broomknot = s.create_oval(hX-10, hY-3, hX, hY+7, fill = "#492510", outline = "#492510")
    leg = s.create_polygon(hX+23, hY+7, hX+21, hY+17, hX+3, hY+24, hX+2, hY+16, hX+11, hY+12, hX+14, hY-1, fill = "#31170a")
    foot = s.create_polygon(hX+2, hY+16, hX+3, hY+24, hX-3, hY+25, hX-2, hY+35, hX-9, hY+34, hX-11, hY+19, fill = "#1b1304")
    undercoat = s.create_polygon(hX+63, hY-38, hX+60, hY-30, hX+27, hY+12, hX+4, hY-4, hX-6, hY-22, fill = "#84141c", outline = "#c5871b", width = 3)
    overcoatY = s.create_polygon(hX-18, hY-16, hX-20, hY-20, hX+44, hY-39, hX+66, hY-34, hX+30, hY-6, fill = "#c5871b")
    overcoat = s.create_polygon(hX-20, hY-20, hX+41, hY-43, hX+63, hY-38, hX+27, hY-10, fill = "#84141c")
    head = s.create_oval(hX+36, hY-82, hX+84, hY-36, fill = "#e6c198", outline = "#e6c198")
    hair = s.create_polygon(hX+39, hY-39, hX+32, hY-64, hX+44, hY-79, hX+61, hY-87, hX+77, hY-79, hX+84, hY-69, hX+54, hY-59, fill = "black")
    hand = s.create_oval(hX+71, hY-29, hX+82, hY-19, fill = "#e6c198", outline = "#e6c198")
    arm = s.create_polygon(hX+41, hY-33, hX+57, hY-28, hX+74, hY-29, hX+75, hY-11, hX+55, hY-8, hX+32, hY-15, fill = "#84141c")
    eye = s.create_oval(hX+69, hY-56, hX+73, hY-52, fill = "black")
    glasses = s.create_oval(hX+64, hY-61, hX+78, hY-47, outline = "black")
    scar = s.create_line(hX+75, hY-71, hX+80, hY-67, hX+77, hY-66, hX+82, hY-59, width = 2, fill = "#e69900")
    bludger = s.create_oval(hX+45,hY-33,hX+95,hY+17, fill = "brown", outline = "brown")
    x = x + 1.5
s.update()
