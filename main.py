import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The Turtle Crossing")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

level = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.check_win_status():
        level += 1
        scoreboard.refresh_scoreboard(level)
        player.start_pos()

    car_manager.create_car()
    car_manager.move_cars(level)

    for car in car_manager.all_cars:
        if car.distance(player.player) < 15:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
