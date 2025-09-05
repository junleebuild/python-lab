from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-220, 260)
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.level = 1
        self.upload_scoreboard()

    def upload_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font= FONT)

    def increase_level(self):
        self.level += 1
        self.upload_scoreboard()


