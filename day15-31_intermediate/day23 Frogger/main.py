import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.update()

player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # every 6th loop create a new car object
    if i % 6 == 0:
        car.create_car()

    car.move()

    # collision detection
    for each_car in car.all_cars:
        if player.distance(each_car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # If the player makes it to the finish line
    if player.ycor() > 279:
        player.player_reset()
        scoreboard.level_up()
        car.increase_speed()

    i += 1
screen.exitonclick()
