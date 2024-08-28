import turtle
import time
# windo
wind=turtle.Screen()
wind.title("pind pong ")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)# للتحديث
#madrab1
ma1=turtle.Turtle()
ma1.speed(0)
ma1.shape("square")
ma1.color("blue")
ma1.shapesize(stretch_wid=7,stretch_len=1)
ma1.penup()# no drawing when moving.
ma1.goto(-350,0)# posision
#madrab2 
ma2=turtle.Turtle()
ma2.speed(0)
ma2.shape("square")
ma2.color("red")
ma2.shapesize(stretch_wid=7,stretch_len=1)
ma2.penup()
ma2.goto(350,0)
#kora 
ko3=turtle.Turtle()
ko3.speed(0)
ko3.shape("square")
ko3.color("white")
ko3.penup()
ko3.goto(0,0)
sp=2
ko3.dx=sp
ko3.dy=sp
# sco
sco1=0
sco2=0
sco=turtle.Turtle()
sco.speed(0)
sco.color("white")
sco.penup()
sco.hideturtle()
sco.goto(0,260)
sco.write(f"player1->{sco1}    player 2->{sco2}" , align="center" ,font=("Courier",15,"normal"))

# fun
def ma1_up():
    y=ma1.ycor()# get the y
    y+=20#  y=y+20
    ma1.sety(y)# set the y
def ma1_dowm():
    y=ma1.ycor()
    y-=20
    ma1.sety(y)

def ma2_up():
    y=ma2.ycor()
    y+=20
    ma2.sety(y)
def ma2_dowm():
    y=ma2.ycor()
    y-=20
    ma2.sety(y)

# ma1_up()
wind.listen()# to control from key pord
wind.onkeypress(ma1_up,"w")
wind.onkeypress(ma1_dowm,"s")
wind.onkeypress(ma2_up,"Up")
wind.onkeypress(ma2_dowm,"Down")
while True:
    wind.update()
    # to move kora
    ko3.setx(ko3.xcor()+ko3.dx)
    ko3.sety(ko3.ycor()+ko3.dy)

    if  ko3.ycor()>290:#top y ==300
        ko3.sety(290)
        ko3.dy*=-1

    if  ko3.ycor()<-290:#dowm y = -300  
        ko3.sety(-290)
        ko3.dy*=-1#revers diriction

    if  ko3.xcor()>390:
        ko3.goto(0,0)# return to center
        ko3.dx*=-1
        sco1+=1
        sco.clear()
        sco.write(f"player1->{sco1}    player 2->{sco2}" , align="center" ,font=("Courier",15,"normal"))

    if  ko3.xcor()<-390:
        ko3.goto(0,0)
        ko3.dx*=-1#revers diriction
        sco2+=1
        sco.clear()
        sco.write(f"player1->{sco1}    player 2->{sco2}" , align="center" ,font=("Courier",15,"normal"))

    if sco1>=5  or sco2>=5: sp*=2
    if sco1>=10 or sco2>=10:sp+=2
    if sco1>=15 or sco2>=15:sp+=2

    if(ko3.xcor()>340 and ko3.xcor()<350 ) and (ko3.ycor()<ma2.ycor()+40 and ko3.ycor()>ma2.ycor()-40):
        ko3.setx(340)
        ko3.dx*=-1

    if(ko3.xcor()<-340 and ko3.xcor()>-350 ) and (ko3.ycor()<ma1.ycor()+40 and ko3.ycor()>ma1.ycor()-40):
        ko3.setx(-340)
        ko3.dx*=-1

    if sco1==20:sco.write(f"player 1->{sco1} is win" , align="center" ,font=("Courier",150,"normal"));print("player 1 win");time.sleep(5);break 
    if sco2==20:sco.write(f"player 2->{sco2} is win" , align="center" ,font=("Courier",150,"normal"));print("player 2 win");time.sleep(5);break
