import turtle as t
import random as random

#기능 - 왼쪽 마우스 버튼 클릭시
# 클릭한 곳까지 이동후 그려짐
def leftclick(x,y):
    global r,g,b
    t.goto(x,y)
    t.pencolor((r,g,b))
    t.down()

def rightclick(x,y):
    t.penup()
    t.goto(x,y)

def midclick(x,y):
    global r,g,b
    tSize = random.randrange(1,10)
    t.shapesize(tSize)
    r= random.random()
    g= random.random()
    b= random.random()


pSize = 10
r=0.0
g=0.0
b=0.0

t.title("거북이")
t.shape("turtle")
t.pensize(pSize)

#onscreenclic(함수명, ?? ) 1은 왼쪽마우스 버튼, 2는 가운데, 3은 오른쪽
t.onscreenclick(leftclick,1)
t.onscreenclick(midclick,2)
t.onscreenclick(rightclick,3)

t.done()
