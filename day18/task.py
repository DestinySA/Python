import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def turtle_random():
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))

def draw_spirograph(size):
    tim.pensize(1)
    for _ in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)

turtle_random()
draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
