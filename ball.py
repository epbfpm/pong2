from turtle import Turtle

UP = 90.0
DOWN = 270.0
RIGHT = 0.0
LEFT = 180.0
SPEED = 3


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(0.5)
        self.penup()
        self.modifier = 0.1
        self.side_collision_modifier = 1
        self.xspd = 2
        self.yspd = 2
        self.spd = 0.01

    def movement(self):
        x = self.xcor() + self.xspd
        y = self.ycor() + self.yspd
        self.setpos(x, y)

    def bounce_y(self):
        self.yspd *= -1

    def bounce_x(self):
        self.xspd *= -1.1
        self.spd *= 0.1

    def reset(self):
        self.setpos(0, 0)
        self.bounce_x()
        self.spd = 0.01
        self.xspd = 2

    # def inertia_modulation_l(self, inertia):
    #     if inertia > 4:
    #         inertia = 4
    #     if inertia < 0:
    #         inertia += self.modifier
    #     else:
    #         inertia -= self.modifier
    #     return inertia
    #
    # def inertia_modulation_r(self, inertia):
    #     if inertia > 4:
    #         inertia = 4
    #     if inertia < 0:
    #         inertia += self.modifier
    #     else:
    #         inertia -= self.modifier
    #     return inertia
