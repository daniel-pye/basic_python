"""
Write a non-fruitful function drawPoly(someturtle, somesides, somesize) which makes a turtle draw a regular polygon. 
"""

import turtle

wn = turtle.Screen()  # Create the canvas
wn.bgcolor("lightgreen")  # Colour the canvas

alex = turtle.Turtle()  # Create the turtle
alex.color("pink")   # Colour the turtle

def drawPoly(t, sides, size):
    for i in range(1, sides + 1):
        t.forward(size)
        t.left(360 / sides)

drawPoly(alex, 8, 50)      
        
        
wn.exitonclick()
