from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = self.create_player()

    def create_player(self):
        player = Turtle()
        player.shape("turtle")
        player.penup()
        player.setheading(90)
        player.color("green")
        player.goto(STARTING_POSITION)
        return player

    def move(self):
        self.player.forward(MOVE_DISTANCE)

    def check_win_status(self):
        if self.player.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def start_pos(self):
        self.player.goto(STARTING_POSITION)
