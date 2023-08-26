from turtle import Turtle, Screen
bob = Turtle()
bob.pensize(5)
bob.pencolor("white")
def forwards():
    bob.forward(10)

def backwards():
    bob.backward(10)

def anti_clock_wise():
    bob.right(-10)

def clock_wise():
    bob.right(10)


def clear():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()



screen = Screen()
screen.bgcolor("brown")
screen.listen()
screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(anti_clock_wise, "a")
screen.onkey(clock_wise, "d")
screen.onkey(clear, "c")

screen.exitonclick()


