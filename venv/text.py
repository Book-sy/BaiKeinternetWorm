from turtle import *

def drawBranch(circlex,circley,branchNum,branchAllNum,lineHeight,name,title,p):
    p.penup()
    p.goto(circlex,circley)
    p.right(360*branchNum/branchAllNum)
    p.penup()
    p.forward(20)
    p.pendown()
    p.forward(lineHeight/2)
    p.write(name, align="center",font=("微软雅黑", 14, "bold"))
    p.forward(lineHeight/2)
    p.penup()
    p.forward(20)
    drawCircle(p)
    p.right(270)
    p.penup()
    p.forward(20)
    p.goto(p.xcor(),p.ycor()-10)
    p.write(title, align="center",font=("微软雅黑", 14-len(name)))
    p.ht

def drawCircle(p = None,circlex = 0,circley = 0):
    if p == None:
        p = Pen()
        p.pendown()
        p.goto(circlex,circley)
    p.penup()
    p.forward(20)
    p.pendown()
    p.left(90)
    p.circle(20, 360)
    p.hideturtle()

for i in range(5):
    p = Pen()
    p.hideturtle()
    p.width(3)
    drawBranch(0,0,i,5,50,"韩硕","牛逼",p)