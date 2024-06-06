from turtle import Turtle
import random
CARS_SPEED = 10

colors = ["red", "blue", "yellow", "green", "purple"]


class Car_manager():
    def __init__(self):
        self.speed = CARS_SPEED
        self.all_cars = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            new_car.setheading(180)
            new_car.goto(400, random.randint(-360, 360))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.fd(self.speed)

    def increase_speed(self):
        self.speed += 5






