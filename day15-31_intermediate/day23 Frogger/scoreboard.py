from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-215, 250)
        self.write(f'Level : {self.score}', align='center', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER\nScore : {self.score}', align='center',
                   font=FONT)

    def level_up(self):
        self.score += 1
        self.update_scoreboard()
