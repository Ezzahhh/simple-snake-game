from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.snake_parts = []
        self.snake_size = 3
        self.create_snake()
        self.head = self.snake_parts[0]
        self.tail = self.snake_parts[-1]

    def create_snake(self) -> None:
        for i in range(self.snake_size):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.speed(0)
            snake.setposition(x=-(20 * i), y=0)
            self.snake_parts.append(snake)

    def add_snake_part(self) -> None:
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.speed(0)
        x_cor = self.tail.xcor()
        y_cor = self.tail.ycor()
        prev_heading = self.tail.heading()
        if prev_heading == UP:
            new_snake.setposition(x=x_cor, y=y_cor - 20)
        elif prev_heading == DOWN:
            new_snake.setposition(x=x_cor, y=y_cor + 20)
        elif prev_heading == LEFT:
            new_snake.setposition(x=x_cor + 20, y=y_cor)
        elif prev_heading == RIGHT:
            new_snake.setposition(x=x_cor - 20, y=y_cor)
        self.snake_parts.append(new_snake)

    def move(self) -> None:
        for seg in range(len(self.snake_parts) - 1, 0, -1):
            prev = self.snake_parts[seg - 1].pos()
            self.snake_parts[seg].goto(prev)
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self) -> None:
        for snk in self.snake_parts:
            snk.clear()
            snk.ht()
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]
