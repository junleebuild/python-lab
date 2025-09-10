from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.speed = MOVE_DISTANCE

    def move(self):
        new_y = self.ycor() + self.speed
        self.goto(self.xcor(), new_y)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reset_turtle()
            return True

        return False
