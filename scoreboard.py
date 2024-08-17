from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.ht()
        self.draw_score()

    def draw_score(self):
        self.write(arg=f"Score: {self.score}", align="center", font=('Courier', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER.", align="center", font=('Courier', 24, 'normal'))

    def add_point(self):
        self.score += 1
        self.clear()
        self.draw_score()

