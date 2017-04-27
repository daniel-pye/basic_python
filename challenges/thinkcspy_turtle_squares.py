""" 
Write a program to draw this. 
Assume the innermost square is 20 units per side, 
and each successive square is 20 units bigger, 
per side, than the one inside it.
"""

import turtle  # import the module

wn = turtle.Screen()  # Create the canvas
wn.bgcolor("lightgreen")  # Colour the canvas

alex = turtle.Turtle()  # Create the turtle
alex.color("pink")   # Colour the turtle

# Draw square functions

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

def newPos(t):
    t.up()
    t.forward(-10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.down()
    
# Draw first square
drawSquare(alex, 20)
newPos(alex)
drawSquare(alex, 40)
newPos(alex)
drawSquare(alex, 60)
newPos(alex)
drawSquare(alex, 80)
newPos(alex)
drawSquare(alex, 100)
newPos(alex)

wn.exitonclick()
