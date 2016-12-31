# Name:    Ciaran McGarrigle
# Module:  Physics For Games
# Course:  Entertainment Systems
# Program: Falling Ball

from visual import *
autoscale = True

# final box, once the ball hits this line (their respective y match) stop the ball
floor = box(pos=(0,-35,0),length=500, height=5, width=10, color =color.blue)
check1 = box(pos=(0,475,0),length=500, height=5, width=10, color =color.yellow)
check2 = box(pos=(0,350,0),length=500, height=5, width=10, color =color.yellow)
check3 = box(pos=(0,225,0),length=500, height=5, width=10, color =color.yellow)
check4 = box(pos=(0,100,0),length=500, height=5, width=10, color =color.yellow)

# Creating the Ball and giving it its paramaters
ball =  sphere(pos=(0,600,0),radius=7.5, color=color.green,make_trail = True,
trail_type="curve")

# Setting up time initial value
t = 0.0

# Setting up dt value
dt = 0.01

# while the position of the ball on the y direction is greater than -25
while ball.pos.y > -25:
    rate(100)
    ball.pos.y = 500-5*(t**2)
    t=t+dt
