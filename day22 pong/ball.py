from turtle import Turtle
from time import sleep


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('green')
        self.shape('square')
        self.speed('slowest')
        self.reset_speed()

    def move(self):
        new_x = self.xcor()+self.x_mod
        new_y = self.ycor()+self.y_mod
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_mod *= -1

    def deflect(self):
        self.x_mod *= -1
        self.increase_speed()

    def reset(self):
        self.deflect()
        self.goto(0, 0)
        sleep(0.5)
        self.reset_speed()

    def reset_speed(self):
        self.x_mod = 0.01
        self.y_mod = 0.01

    def increase_speed(self):
        self.x_mod *= 1.5
        self.y_mod *= 1.5
