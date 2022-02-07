from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.refresh_scoreboard(1)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def refresh_scoreboard(self, level):
        self.goto(-215, 250)
        self.clear()
        self.write(f"Level: {level}", align="center", font=FONT)
