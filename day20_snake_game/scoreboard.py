from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", False, ALIGNMENT, FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)
