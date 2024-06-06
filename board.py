from turtle import Turtle as t


class Board(t):

    def __init__(self):
        super().__init__()
        self.Highest = 0
        self.level = 1
        self.display()

    def display(self):
        self.penup()
        self.hideturtle()
        self.goto(-380, 360)
        self.clear()
        self.write(f"Level :{self.level}", align="left", font=("Arial", 18, "normal"))



    def level_up(self):
        self.level += 1
        self.display()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
