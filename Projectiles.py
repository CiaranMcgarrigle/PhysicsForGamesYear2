# Name:    Ciaran McGarrigle
# Module:  Physics For Games
# Course:  Entertainment Systems
# Program: Projectiles

from visual import *
autoscale = True

# Creation of floor object and its parameters
floor = box(length=100, height=5, width=10, color =color.blue,)

# Creation of Ball object and its parameters 
ball =  sphere(pos=(-50,10,0),radius=2, color=color.yellow,make_trail =True,
trail_type ="curve")

# launch the ball in the direction of the velocity vector
ball.velocity = vector(5,15,0)

# Setup of value for g (Acceleration due to Gravity)
g = 9.8

#Setup of value for e
e = 0.95

# Setup for value of dt
dt = 0.01

# Setup of value for time
t=0

# Update the position of the ball with its new value based on its current position
# with the velocity of the ball multiplied by the change in time (delta time).  If the
# ball hits the floor then bounce it back up from the ground.
while ball.pos.x<75:
    rate(1000)
    ball.pos =  ball.pos + ball.velocity*dt
    if ball.y < ball.radius+floor.height/2:
        ball.velocity.y = -e*ball.velocity.y
    else:
        ball.velocity.y = ball.velocity.y - g*dt
    t=t+dt
