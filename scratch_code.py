# daily work
# 100DaysOfCodeJournal
# python3 scratch_code.py

from turtle import Turtle, Screen


def draw_square(some_turtle):

    for _ in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)


def draw_art():

    # Turtle Brad
    brad = Turtle(shape="turtle")
    brad.color("yellow")
    brad.pensize(2)
    brad.speed("fast")

    for _ in range(36):
        draw_square(brad)
        brad.right(10)

    # Turtle Angie
    angie = Turtle(shape="turtle")
    angie.color("orange")
    angie.pensize(2)
    angie.speed(10)

    size = 1

    for _ in range(300):
        angie.forward(size)
        angie.right(91)
        size += 1


window = Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()
