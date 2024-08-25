#Pong Game
#author: Sehajleen Kaur

from turtle import *
from random import randint, random

#coordinates of the window
X, Y = 500, 500

collision = 0
start = 0

#set the changes in x and y coordinates to be random
dX = random() + 1
dY = random() + 1

#initialising screen
screen = Screen()
screen.setup(X,Y)
screen.title("Pong!")
screen.bgpic('b.png')

#printing text on top
t0 = Turtle()
t0.hideturtle()
t0.color('aquamarine')
t0.speed(8)
t0.penup()
t0.goto(0,Y//2-20)
t0.write("Press 'p' to play!", True, align="center", font=('Courier', 12, 'italic'))
t0.penup()

#defining the attributes of the slider 
t1 = Turtle()
t1.hideturtle()
sliderH, sliderW = 90,20
screen.register_shape("line", ((-sliderW//2,-sliderH//2), (-sliderW//2,sliderH//2), (sliderW//2,sliderH//2), (sliderW//2,-sliderH//2)))
t1.shape('line')
t1.speed(0)
t1.color('purple2')
t1.setheading(90)
t1.penup()
t1.goto(-X//2 + 10, 0)
t1.showturtle()
 
#defining the functions for movements of the slider to go up and down
def go_up():
    t1.fd(10)

def go_down():
    t1.bk(10)

#defning the function to start the game
def start_game():
    global start
    start = 1

#calling out the funtions when specific keys are pressed
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(start_game, 'p')


#defining the atributes of the ball 
t2 = Turtle()
t2.shape('circle')
t2.speed(0)
t2.color('cyan2')
t2.penup()
ballX, ballY = 0, 0
t2.goto(ballX,ballY)
t1.setheading(90)

#defining the function for the path of the ball
def move_t2():
  global sliderH, sliderW
  global X, Y
  global ballX, ballY
  global dX, dY
  global collision
  global start

  t2.goto(ballX, ballY)
  sliderX, sliderY = t1.pos()

#when the ball hits the slider
  if ballY >= (sliderY - sliderH//2)and ballY <= (sliderY + sliderH//2) and ballX <= -X//2 + sliderW + 10:
    if collision == 0:
      dX = -dX
      collision = 1

#when the ball misses the slider
  if ballY <= (sliderY - sliderH//2) or ballY >= (sliderY + sliderH//2):
    if ballX <= -X//2 + sliderW + 10 -5:
      start = 0
    
  if ballX >= -X//2 + sliderW + 10:
    collision = 0
    
#when the ball has to bounce after collision
  if ballX > X//2 -10:
    dX = -dX

  if ballY > Y//2 - 10:
    dY = -dY

  if ballY < -Y//2 + 10:
    dY = -dY       

  if start == 1:
    ballX += dX
    ballY += dY

  else:
      ballX = 0
      ballY = 0
    
  screen.ontimer(move_t2,1)

#calling out functions to start the game
move_t2()
screen.listen()
screen.mainloop()
