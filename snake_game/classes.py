from turtle import Turtle
import random
import time
move_distance=20
angle=90
direction="R"
class snake:
    def __init__(self):
        self.body=[]
    def creat_snake(self):
        for number in range(3):
            Snake=Turtle("square")
            self.body.append(Snake)
    def creat_new_piece(self):
        Snake=Turtle("square")
        Snake.hideturtle()
        Snake.penup()
        self.body.append(Snake)
    def pen_up(self):
        for snake in self.body:
            snake.penup()
    def setposition(self):
        self.pen_up()
        x=0
        y=0
        for snake in self.body:
            snake.setpos(x,y)
            x-=move_distance
    def move_forward(self):
        for snake in range(len(self.body)-1 , 0 , -1):
            x=self.body[snake-1].xcor()
            y=self.body[snake-1].ycor()
            self.body[snake].goto(x,y)
        self.body[-1].showturtle()
        self.body[0].forward(move_distance)
    def right(self):
        global direction
        if direction!="L":
            self.body[0].setheading(0)
            direction="R"
    def left(self):
        global direction
        if direction!="R":
            self.body[0].setheading(180)
            direction="L"
    def Up(self):
        global direction
        if direction!="D":
            self.body[0].setheading(90)
            direction="U"
    def down(self):
        global direction
        if direction!="U":
            self.body[0].setheading(270)
            direction="D"
    def reset_snake(self):
        for snake in self.body:
            snake.hideturtle()
        self.body.clear()
        self.creat_snake()
        self.setposition()
class Fruit(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
    def appear(self):
        n=-280
        pos=[]
        while n<290:
            pos.append(n)
            n+=20
        x=random.choice(pos)
        y=random.choice(pos)
        self.setposition(x,y)
        self.showturtle()
class scorechecker(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(x=0,y=320)
        self.score=0
    def read_score(self):
        with open("highscore.txt", mode="r") as tx:
            self.highscore=int(tx.read())
    def write_score(self):
        self.read_score()
        self.write(f"score :{self.score} highscore : {self.highscore}",False)
    def update_highscore(self):
        self.highscore=str(self.score)
        with open("highscore.txt", mode="w") as tx:
                tx.write(self.highscore)
    def detect_eaten(self,fr,sn):
        self.score+=1
        self.clear()
        self.write_score()
        fr.appear()
        sn.creat_new_piece()
    def write_gameOver(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER",False) 
    def reset_the_game(self,SN,fr):
        self.score=0
        time.sleep(1)
        self.clear()
        self.goto(0,320)
        self.write_score()
        SN.reset_snake()
        fr.appear()
    def check_lost(self,sn,fr,SN):
        if sn[0].xcor()<-290 or sn[0].xcor()>290 or sn[0].ycor()<-290 or sn[0].ycor()>290:
            self.write_gameOver()
            if self.score>int(self.highscore):
                self.update_highscore()
            self.reset_the_game(SN,fr)
        for snake in sn[1:]:
            if sn[0].position()==snake.position():
                self.write_gameOver()
                if self.score>int(self.highscore):
                    self.update_highscore()
                self.reset_the_game(SN,fr)
class wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(x=-300,y=-300)
        self.pendown()
    def draw_wall(self):
        self.speed(10)
        for x in range(4):
            self.forward(600)
            self.left(angle)
