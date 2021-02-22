import colorgram
import turtle
import random

turtle.screensize(500)
turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed(1)


def get_colours():
    colours = colorgram.extract('images/spot_painting.jpg', 30)
    # make a tuple of each set of rgb numbers for every Colour object in the list
    rgb_colours = [tuple((colour.rgb.r, colour.rgb.g, colour.rgb.b)) for colour in colours]
    return rgb_colours


def random_colour():
    chosen_colour = random.choice(get_colours())
    return chosen_colour


def make_dot():
    timmy.dot(20, random_colour())
    timmy.penup()
    timmy.forward(50)


def start_turtle():
    timmy.penup()
    timmy.setpos(-300, -300)


def new_line():
    y = timmy.ycor() + 50
    x = timmy.xcor()
    timmy.left(180)
    timmy.setposition(x, y)
    timmy.forward(50)


def start_circuit():
    for _ in range(12):
        make_dot()

    new_line()


start_turtle()

for _ in range(12):
    start_circuit()


screen = turtle.Screen()
screen.exitonclick()