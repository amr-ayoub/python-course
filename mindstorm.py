# Draw square

import turtle

window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()

    
def square():
    for x in range(0,4):
        brad.forward(100)
        brad.right(90)



def circle():
    brad.circle(100,None,None)
    
    
def triangle():
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(135)
    brad.forward(142)



square()
circle()
triangle()
window.exitonclick()

