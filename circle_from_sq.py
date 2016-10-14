import turtle

window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()

    
def square():
    for x in range(0,4):
        brad.forward(100)
        brad.right(90)




for i in range(0,36):
    square()
    brad.right(10)


window.exitonclick()
