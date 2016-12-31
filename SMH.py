# Name:    Ciaran McGarrigle
# Module:  Physics For Games
# Course:  Entertainment Systems
# Program: Simple Harmonic Motion

from visual import *

autoscale = True

# length of distance between the ceiling and the ball's position from the celling
l = 0.6125

# Setup for value of g (Acceleration due to Gravity)
g = 9.8

# Setup for caluclation to get omega of the ball
omega = sqrt((g/l))

# Setup value of time
t = 0

# Setup value of dt
dt = 0.01

# Creation of floor object and its parameters
floor = box(pos=(0,10,0), length=7.5, height=1, width=7.5, color = color.red)

# Creation of ball object along with its parameters
ball = sphere(pos=(1, l ,0), radius=1)

# infinite loop
while True:
    rate(100)

    # set the ball position x equal to (0.4)x(cos((omega)x(time)))+(0.125*(sin((omega)(t))))
    ball.pos.x = (0.4*(cos((omega*t)))) + (0.125*(sin(omega*t)))
    ball.pos.y = (l/2)*ball.pos.x**2
    
    t+=dt
