from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier", 18, "bold"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("D:\Python\Intermediate\day-021-project\my-snake-game\data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:  {self.score}   High Score: {self.highscore}",
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("D:\Python\Intermediate\day-021-project\my-snake-game\data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"GAME OVER:(",
    #                align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
