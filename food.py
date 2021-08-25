from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(x=randint(-260, 260), y=randint(-260, 260))

    def new_location(self) -> None:
        self.goto(x=randint(-260, 260), y=randint(-260, 260))
