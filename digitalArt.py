
import turtle
radius = int(input("Enter circle radius as an integer: "))
drawSpeed = int(input("Enter speed for circle to be drawn: "))
circleColor = input("Enter the color of the circle: ")
circleDrawer = turtle.Turtle()
circleDrawer.speed(drawSpeed)
circleDrawer.color(circleColor)
circleDrawer.circle(radius)
turtle.done()