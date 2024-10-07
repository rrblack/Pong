import time
import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0,0))
scoreboard = Scoreboard()

paddle_speed = 20
ball_speed = 10

left_score = 0
right_score = 0

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")

gameon = True

while gameon:
    if r_paddle.moving_up:
        new_y = r_paddle.ycor() + paddle_speed
        if new_y < screen.window_height() // 2 - 30:  # Prevents moving off-screen
            r_paddle.goto(r_paddle.xcor(), new_y)
    if r_paddle.moving_down:
        new_y = r_paddle.ycor() - paddle_speed
        if new_y > -screen.window_height() // 2 + 50:  # Prevents moving off-screen
            r_paddle.goto(r_paddle.xcor(), new_y)
    if l_paddle.moving_up:
        new_y = l_paddle.ycor() + paddle_speed
        if new_y < screen.window_height() // 2 - 30:  # Prevents moving off-screen
            l_paddle.goto(l_paddle.xcor(), new_y)
    if l_paddle.moving_down:
        new_y = l_paddle.ycor() - paddle_speed
        if new_y > -screen.window_height() // 2 + 50:  # Prevents moving off-screen
            l_paddle.goto(l_paddle.xcor(), new_y)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
        left_score += 1

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()
        right_score += 1

    if left_score >= 10 or right_score >= 10:
        gameon = False
        scoreboard.game_over()
        ball.hideturtle()

    time.sleep(.02)
    screen.update()


screen.exitonclick()
