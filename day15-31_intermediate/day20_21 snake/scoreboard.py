from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_hscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        print(self.high_score)

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            print('if')
            self.high_score = self.score
            self.score = 0
            self.write_hscore()
            self.update_scoreboard()

    def read_hscore(self):
        with open('data.txt', mode='r') as data_file:
            self.high_score = int(data_file.read())

    def write_hscore(self):
        with open('data.txt', mode='w') as data_file:
            data_file.write(str(self.high_score))
