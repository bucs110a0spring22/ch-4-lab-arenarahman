import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def setupWindow(mywindow=None):
  wn = turtle.Screen()
  wn.bgcolor('lightblue')
  wn.mode('world')
  wn.reset()
  wn.setworldcoordinates(-360,-1,360,1)
  
def setupAxis(myturtle=None):
  for i in range(-360,360):
    myturtle.goto(i,0)
  myturtle.goto(0,-1)
  myturtle.goto(0,1)

def drawSineCurve(myturtle=None):
  for angle in range(-360,360):
    y = math.sin(math.radians(angle))
    myturtle.goto(angle,y)
    print(y)

def drawCosineCurve(myturtle=None):
  for angle in range(-360,360):
    y = math.cos(math.radians(angle))
    myturtle.goto(angle,y)

def drawTangentCurve(myturtle=None):
  for angle in range(-360,360):
    y = math.tan(math.radians(angle))
    myturtle.goto(angle,y)

    
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
