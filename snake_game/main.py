from turtle import Screen, exitonclick, onkey 
import time
from classes import scorechecker, snake,Fruit,scorechecker,wall
screen=Screen()
screen.setup(width=700,height=700)
screen.title("snake game")
my_snake=snake()
my_fruit=Fruit()
my_score=scorechecker()
my_wall=wall()
screen.tracer(0)
my_wall.draw_wall()
screen.listen()
screen.onkey(my_snake.right,"Right")
screen.onkey(my_snake.left,"Left")
screen.onkey(my_snake.Up,"Up")
screen.onkey(my_snake.down,"Down")
my_snake.creat_snake()
my_snake.setposition()
my_fruit.appear()
my_score.write_score()
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_snake.move_forward()
    if my_snake.body[0].distance(my_fruit)<15:
        my_score.detect_eaten(my_fruit,my_snake)
    my_score.check_lost(my_snake.body,my_fruit,my_snake)
exitonclick()