from turtle import Turtle, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(500, 400)
user_bet = my_screen.textinput(title='Make your bet', prompt='Which colour turtle will win this race? : ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [-100, -60, -20, 20, 60, 100]

turtle_objects = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_pos[turtle_index])
    new_turtle.pendown()
    turtle_objects.append(new_turtle)
# this sets while loop condition to true only if there is a user bet variable
if user_bet:
    is_race_on = True

while is_race_on:
    for contestant in turtle_objects:
        distance = random.randint(0, 10)
        contestant.forward(distance)
        if contestant.xcor() > 230:
            winner = contestant.pencolor()
            if winner == user_bet:
                print('Your turtle is the winner!!')
            else:
                print(f"Sorry, you've lost, the Winning turtle is {winner}")
            is_race_on = False
my_screen.exitonclick()
