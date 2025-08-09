import pgzrun
WIDTH=1200
HEIGHT=800
mbox=Rect(0,0,1200,100)
qbox=Rect(10,120,800,150)
tbox=Rect(850,120,300,150)
obox1=Rect(10,280,400,200)
obox2=Rect(420,280,400,200)
obox3=Rect(10,280,400,200)
obox4=Rect(10,280,400,200)
def draw():
    screen.draw.filled_rect(mbox,"white")
    screen.draw.filled_rect(qbox,"blue")
    screen.draw.filled_rect(tbox,"darkgreen")
    screen.draw.filled_rect(obox1,"purple")
    screen.draw.filled_rect(obox2,"purple")
pgzrun.go()