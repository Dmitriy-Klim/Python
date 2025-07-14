# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 14:22:43 2025

@author: sorok
"""

from turtle import Screen, Turtle
import time

class SScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1250, height=750)
        self.screen.bgcolor("black")
        self.screen.title('The Pong')
        self.screen.tracer(0)
        self.screen.listen()
    
    def exit(self):
        self.screen.exitonclick()
    
    def update(self):
        self.screen.update()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('blue')
        self.hideturtle()

    
    def update_scoreboard(self):
        self.clear()
        self.color('blue')
        self.hideturtle()
        self.penup()
        self.goto(-600, 320)
        self.pendown()
        self.pensize(5)
        self.goto(-320, 320)
        self.goto(600, 320)
        self.goto(600, 370)
        self.goto(-600, 370)
        self.goto(-600, 320)
        self.penup()
        self.goto(-460, 328)
        self.color('yellow')
        self.write(f"Player  -  {self.l_score}", align="center", font=("Courier", 20, "bold"))
        self.goto(430, 328)
        self.write(f"{self.r_score}  -  Computer", align="center", font=("Courier", 20, "bold"))
    
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()    
        
class STurtle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0.0, 285)
        self.pendown()
        self.goto(0, -285)
    
    def borders(self):
        marker = Turtle()
        marker.color('white')
        marker.hideturtle()
        marker.penup()
        marker.goto(-600, 300)
        marker.pendown()
        marker.color('red')
        marker.goto(-600, -300)
        marker.color('white')
        marker.goto(-300, -300)
        marker.color('white')
        marker.goto(600, -300)
        marker.color('red')
        marker.goto(600, 300)
        marker.color('white')
        marker.goto(-600, 300)
        marker.penup()
        marker.goto(0, -50)
        marker.color('darkGrey')
        marker.write("P    O    N    G", align="center", font=("Arial", 64, "bold"))

class Paddle(Turtle):
    pass        

class SDot(Turtle):
    def __init__(self):
        super().__init__()
        #self.hideturtle()
        self.color('yellow')
        self.shape('circle')
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.05
        self.penup()
        self.goto(0, 0)
        self.xcor()
        self.ycor()
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()

class SWall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=7.5)
        self.shape('square')
        self.color('white')
        self.speed = 30
            
    def pc_wall_moving(self, y):
        time.sleep(0.2)
        self.goto(580, y)

    def go_up(self):
        y = self.ycor() + self.speed
        if y < 270:
            self.sety(y)
    
    def go_down(self):
        y = self.ycor() - self.speed
        if y > -270:
            self.sety(y)


    
screen = SScreen()
separator = STurtle()
separator.borders()

pc_wall = SWall()
scoreboard = ScoreBoard()
scoreboard.update_scoreboard()
ball = SDot()

player_wall = SWall()
player_wall.goto(-580, 0)
player_wall.shapesize(stretch_len=0.5, stretch_wid=4.0)

screen.screen.listen()
screen.screen.onkey(player_wall.go_up, "Up")
screen.screen.onkey(player_wall.go_down, "Down")

y = 10
while True:
    screen.update()    
    ycoord = pc_wall.ycor() + y
    pc_wall.pc_wall_moving(ycoord)
    if ycoord >= 220 or ycoord <= -220:
        y *= -1
    
    ball.move()
    # Обнаружение столкновения с верхней/нижней стеной
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Обнаружение столкновения с ракетками
    if ball.distance(player_wall) < 50 or ball.distance(pc_wall) < 70:
        ball.bounce_x()
    

    # Обнаружение пропуска мяча
    if ball.xcor() > 610:
        ball.reset_position()
        scoreboard.l_point()
        
    if ball.xcor() < -610:
        ball.reset_position()
        scoreboard.r_point()
    

screen.exit()     
