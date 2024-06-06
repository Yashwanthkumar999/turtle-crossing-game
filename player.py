from turtle import Turtle

STARTING_POSITION = (0, -380)


class Player(Turtle):
    def __init__(self):

        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def go(self):
        self.forward(10)

    def down(self):
        self.backward(10)

    def goto_start(self):
        self.goto(STARTING_POSITION)



