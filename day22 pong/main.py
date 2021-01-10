from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    # collision detection with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Collision detection with paddles
    elif (ball.distance(r_paddle) < 50 and ball.xcor() > 335 or
          ball.distance(l_paddle) < 50 and ball.xcor() < -335):
        ball.deflect()
    # Right Paddle Misses
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
    # Light Paddle Misses
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()
