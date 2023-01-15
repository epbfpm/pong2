from turtle import Turtle
from time import sleep

SPEED = 10


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.setpos(x, y)
        self.shapesize(3, 0.5)
        self.aispeed = 10

    def ypos(self, ball):
        return self.ycor() + 35 > ball > self.ycor() - 35

    def go_up(self):
        if (self.ycor() + SPEED) > 270:
            self.sety(270)
        else:
            self.sety(self.ycor() + SPEED)

    def go_down(self):
        if (self.ycor() - SPEED) < -270:
            self.sety(-270)
        else:
            self.sety(self.ycor() - SPEED)

    def ai_go_up(self, x_ball):
        if (self.ycor() + SPEED) > 270:
            self.sety(270)
        else:
            self.sety(self.ycor() + (round(x_ball/100) * (SPEED * (0.1 * int(self.aispeed)))))

    def ai_go_down(self, x_ball):
        if (self.ycor() - SPEED) < -270:
            self.sety(-270)
        else:
            self.sety(self.ycor() - (round(x_ball/100) * (SPEED * (0.1 * int(self.aispeed)))))



