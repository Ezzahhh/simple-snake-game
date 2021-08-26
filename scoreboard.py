from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(
            arg=f"Score: {self.score}",
            move=True,
            align=ALIGNMENT,
            font=FONT,
        )

    def add_score(self) -> None:
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.goto(0, 270)
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            move=True,
            align=ALIGNMENT,
            font=FONT,
        )

    # def game_over(self) -> None:
    #     self.goto(0, 0)
    #     self.write(
    #         arg=f"GAME OVER!",
    #         move=True,
    #         align=ALIGNMENT,
    #         font=FONT,
    #     )

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
