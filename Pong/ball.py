from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse the y-direction
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the x-direction
        self.x_move *= -1


    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
