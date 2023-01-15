from turtle import Turtle


class Tracer(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.setpos(-400, 300)
        self.pendown()
        self.setpos(-400, -300)
        self.setpos(400, -300)
        self.setpos(400, 300)
        self.setpos(-400, 300)


class ScoreBoard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.sety(300)
        self.setx(-50 * side)
        self.write(arg='0', font=('Arial', 60, 'normal'))

    def update(self, score):
        self.clear()
        self.write(arg=score, font=('Arial', 60, 'normal'))
