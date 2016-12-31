# Name:    Ciaran McGarrigle
# Module:  Physics for Games
# Course:  Entertainment Systems
# Project: Spiral.py

from visual import *

# Creation of the moving Ball object and its parameters
ball = sphere(pos=(5, 0,0),radius=0.2, color=color.green, make_trail = True, trail_type = "curve")

# Creation of the stationary Ball object and its parameters
b = sphere(pos=(0, 0, 0), radius=0.2, color=color.blue)

# Creation of the arrow object and its parameters
velocityArrow = arrow(pos=(0,0,0), axis=(5,0,0), shaftwidth=.2)
autoscale = True

# Setup of value for dt
dt = 0.01

# Setup of value for Time
t = 0

# Ehile t is less than 5
while t<5:
    rate(100)

    # Line of code to make the ball move around in a circle
    ball.pos = vector(5*cos(2*t), 5*sin(2*t), ball.pos.z+dt)

    # Move the arrow pointer
    velocityArrow.axis = ball.pos

    # New value of t is equal to t's current value plus dt
    t=t+dt
