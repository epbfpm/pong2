from turtle import Screen
from ball import Ball
from paddle import Paddle
from ui import *
from time import sleep

# global variables
left_score = 0
right_score = 0

# screen
screen = Screen()
screen.title("Pong")
screen.colormode(255)
screen.screensize(800, 600, '#000000')
screen.listen()
screen.tracer(0)

# fixed elements
l_paddle = Paddle(-380, 0)
r_paddle = Paddle(380, 0)
court = Tracer()

# moving elements
ball = Ball()
l_board = ScoreBoard(1)
r_board = ScoreBoard(-1)

# movement
screen.listen()
screen.onkeypress(l_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down, "Down")
screen.listen()

# difficulty selector
lang = screen.textinput('Language/Idioma', 'Input en for english. Insira br para portugues')
if lang == 'en':
    r_paddle.aispeed = screen.numinput('Difficulty', 'Choose a difficulty: 1, 2 or 3', default=2, minval=1, maxval=3)
elif lang == 'br':
    r_paddle.aispeed = screen.numinput('Dificuldade', 'Escolha uma dificuldade: 1, 2 ou 3', default=2, minval=1, maxval=3)

# game on
game_on = True
while game_on:
    sleep(ball.spd)
    screen.update()
    ball.movement()
    screen.listen()
    # ai
    if ball.ycor() > r_paddle.ycor() and ball.heading() == 0 and ball.xcor() > -100:
        r_paddle.ai_go_up(ball.xcor())
    elif ball.ycor() < r_paddle.ycor() and ball.heading() == 0 and ball.xcor() > -100:
        r_paddle.ai_go_down(ball.xcor())

    # change direction on paddle impact
    if ball.xcor() < - 360 and l_paddle.ypos(ball.ycor()):
        ball.right(180)
        ball.bounce_x()

    if ball.xcor() > 360 and r_paddle.ypos(ball.ycor()):
        ball.right(180)
        ball.bounce_x()

    # change direction on side impact
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # score
    if ball.xcor() > 400:
        ball.reset()
        left_score += 1
        l_board.update(left_score)

    if ball.xcor() < -400:
        ball.reset()
        right_score += 1
        r_board.update(right_score)

screen.exitonclick()
