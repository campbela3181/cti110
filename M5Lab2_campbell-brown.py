#CTI 110
#M5Lab2- Initials
#Alicia Campbell-Brown
#10-20-2017
#This program uses the turtle graphics to write my initials

#Sets the appearance of the window and the turtles
import turtle
win = turtle.Screen()
win.bgcolor('blue')
alicia = turtle.Pen()
brown = turtle.Pen()
alicia.shape('turtle')
brown.shape('turtle')
alicia.pencolor('red')
brown.pencolor('red')
alicia.pensize('5')
brown.pensize('5')

#Gets the alicia turtle into place
alicia.penup()
alicia.backward(200)
alicia.pendown()

#writes the A
alicia.width(10)
alicia.left(70)
alicia.forward(100)
alicia.right(140)
alicia.forward(100)
alicia.backward(50)
alicia.right(110)
alicia.forward(39)

#Writes the B
brown.width(10)
brown.left(90)
brown.forward(110)
brown.right(125)
brown.forward(30)
brown.right(55)
brown.forward(25)
brown.right(55)
brown.forward(30)

brown.left(125)
brown.forward(45)
brown.right(70)
brown.forward(20)
brown.right(70)
brown.forward(45)
brown.left(160)
brown.penup

win.mainloop()



