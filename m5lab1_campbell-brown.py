# CTI 110
#M5Lab1- Turtle Square & Rectangle
# Alicia Campbell-Brown
# October 20, 2017
# This program uses turtle graphics to draw a square and a triangle

#Sets the window appearance
import turtle
win = turtle.Screen()
win.bgcolor('skyblue')
triangle = turtle.Pen()
square = turtle.Pen()
square.shape('turtle')
triangle.shape('turtle')
triangle.pencolor('red')
square.pencolor('green')
triangle.pensize('5')
square.pensize('5')

#Moves the triangle turtle
triangle.penup()
triangle.backward(200)
triangle.pendown()

#Draws the square
for i in range(4):
    square.forward(100)
    square.left(90)

#Draws the triangle
for i in range(3):
    triangle.forward(100)
    triangle.left(120)


win.mainloop()




