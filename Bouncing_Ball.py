# Name:    Ciaran McGarrigle
# Module:  Physics For Games
# Course:  Entertainment Systems
# Program: Bouncing_Ball.py

from visual import *

autoscale = True

# Creation of the Floor object and its parameters
floor = box(length=100, height=5, width=10, color =color.green,)

# Creation of the Ball object and its parameters
ball =  sphere(pos=(-40,70,0),radius=2, color=color.blue,make_trail =True, trail_type ="curve")

# Velocity vector to move the ball to the right and in a downward motion
ball.velocity = vector(2,-2,0)

# Setup of value for g (Acceleration due to Gravity)
g = 9.8

#Setup of value for e
e = 0.95

# Setup of value for dt
dt = 0.01

# Setup of value for time
t=0

# Code to make the ball bounce along the table
while ball.pos.x<50:
    rate(100)

    # Move the ball along the x and y axis by taking the ball.pos value and
    # updating it by adding the balls velocity multiplied by the change in time
    ball.pos =  ball.pos + ball.velocity*dt

    # Code to bounce the ball upwards if the ball and table collide
    if ball.y < ball.radius+floor.height/2:
        ball.velocity.y = -e*ball.velocity.y

    # Code to bounce the ball downward with respect to g
    else:
        ball.velocity.y = ball.velocity.y - g*dt

    # Code to update time by adding current t to dt.
    t=t+dt
