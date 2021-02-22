import turtle
import random

turtle.screensize(500)
turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def make_circle():
    timmy.pencolor(random_color())
    timmy.circle(100)
    timmy.right(10)


def make_spirograph():
    for _ in range(36):
        make_circle()


make_spirograph()

screen = turtle.Screen()
screen.exitonclick()