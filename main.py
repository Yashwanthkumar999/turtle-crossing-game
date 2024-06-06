from turtle import Turtle, Screen
import time
from player import Player
from cars_animation import Car_manager
from board import Board
sc = Screen()
sc.title("Help turtle to cross ")
sc.setup(800, 800)
sc.bgcolor("white")


sc.tracer(0)
player = Player()
car = Car_manager()
board = Board()


sc.listen()

sc.onkey(player.go, "Up")
sc.onkey(player.down,"Down")
game_on = True
while game_on:

    time.sleep(0.1)
    sc.update()

    car.create_car()
    car.move_car()

    for i in car.all_cars:

        if i.distance(player) < 20:
            board.game_over()
            game_on = False

    if player.ycor() > 380:
        player.goto_start()

        board.level_up()
        car.increase_speed()



sc.exitonclick()