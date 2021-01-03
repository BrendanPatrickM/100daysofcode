import turtle
import random

timmy = turtle.Turtle()

timmy.shape('arrow')
turtle.colormode(255)
colours = ['pale turquoise','light sky blue','orange red','deep sky blue','misty rose']


# def draw_shape(sides):
#
#      angle = 360/float(sides)
#      print(angle)
#      for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for sides in range(3,11):
#     timmy.color(random.choice(colours))
#     draw_shape(sides)
#
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


angles = [0, 90, 180, 270]
timmy.pensize(10)
#timmy.speed(0)
for _ in range(100):
    timmy.color(random_color())
    timmy.setheading(random.choice(angles))
    timmy.forward(30)




screen = turtle.Screen()
screen.exitonclick()
