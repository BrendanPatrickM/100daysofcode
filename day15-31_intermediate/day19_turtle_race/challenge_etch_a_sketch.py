from turtle import Turtle, Screen


timmy = Turtle()
my_screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


my_screen.listen()

my_screen.onkey(key='w', fun=move_forward)
my_screen.onkey(key='s', fun=move_backward)
my_screen.onkey(key='a', fun=turn_left)
my_screen.onkey(key='d', fun=turn_right)
my_screen.exitonclick()
