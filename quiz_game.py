import pgzrun
WIDTH=1200
HEIGHT=800
mbox=Rect(0,0,1200,100)
qbox=Rect(20,120,800,150)
tbox=Rect(860,120,300,150)
obox1=Rect(20,290,390,200)
obox2=Rect(430,290,390,200)
obox3=Rect(20,510,390,200)
obox4=Rect(430,510,390,200)
sbox=Rect(860,290,300,420)
ol=[obox1,obox2,obox3,obox4]
tns=10
score=0
file1="gkq.txt"
gameo=False
questions=[]
indexn=0
qc=0
def draw():
    screen.draw.filled_rect(mbox,"black")
    screen.draw.filled_rect(qbox,"blue")
    screen.draw.filled_rect(tbox,"darkgreen")
    screen.draw.filled_rect(obox1,"purple")
    screen.draw.filled_rect(obox2,"purple")
    screen.draw.filled_rect(obox3,"purple")
    screen.draw.filled_rect(obox4,"purple")
    screen.draw.filled_rect(sbox,"darkgreen")
    #textboxes
    message="Welcome to the Quiz!"
    screen.draw.textbox(message,mbox,color="white")
    screen.draw.textbox(str(tns),tbox,color="white")
    screen.draw.textbox("SKIP",sbox,color="white",angle=-90)
    screen.draw.textbox(question[0].strip(),qbox,color="white")
    ic=1
    for i in ol:
     screen.draw.textbox(question[ic].strip(),i,color="white")  
     ic+=1 
#marquee effect
def move():
    mbox.x-=5
    if mbox.right<90:
        mbox.left=1000
def update():
    move()
def time():
    global tns
    if tns>0:
        tns-=1
    else:
        go()
def ca():
    global tns, question, score, questions
    score+=1
    if questions:
        question=rn()
        tns=10
    else:
        go()
        
def read():
    global qc,indexn,questions
    rf=open(file1,"r")
    for question in rf:
        questions.append(question)
        qc+=1
    rf.close()
def rn():
    global indexn
    indexn+=1
    return questions.pop(0).split(",")
def on_mouse_down(pos):
    ind=1
    for i in ol:
        if i.collidepoint(pos):
            if ind==int(question[5]):
                ca()
            else:
                go()        
        ind+=1      
    if sbox.collidepoint(pos):
        skip()
def go():
    global question, tns, gameo
    gameo=True
    tns=0
    msg=f"Game over,your score is {score}"
    question=[msg,"-","-","-","-",5]
def skip():
    global question, tns, questions
    if questions and not gameo:
        question=rn()
        tns=10
    else:
        go()
read()
question=rn()
clock.schedule_interval(time,1)  
pgzrun.go()
