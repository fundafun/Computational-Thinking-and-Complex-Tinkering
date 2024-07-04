import turtle
import random  # NEW!


sideLength = float(input("Enter the line length: "))

lineColor = input("Enter a line color: ")

drawer = turtle.Turtle()

drawer.color(lineColor)

drawer.speed(1)

for line in range(20):
    randVal = random.randint(1, 180)
    drawer.forward(sideLength)  
    drawer.right(randVal)      

turtle.done()
