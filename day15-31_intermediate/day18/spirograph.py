import turtle
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


timmy = turtle.Turtle()
timmy.shape('arrow')
turtle.colormode(255)
timmy.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)


draw_spirograph(5)








screen = turtle.Screen()
screen.exitonclick()
