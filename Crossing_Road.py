# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 10:50:59 2025

@author: sorok
"""

import time
from turtle import Turtle, Screen
import random
#===================================================
STARTING_POSITION = (0, -300)
MOVE_DISTANCE = 10
FINISH_LINE = 270
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
    
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
#===================================================
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_cars(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
            
#===================================================
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.update_scorebnoard()
    
    def update_scorebnoard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.update_scorebnoard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
#===================================================
screen = Screen()
screen.setup(width=600, height=700)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move_cars()
    
    #Detecting collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #Detectins succesful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    
screen.exitonclick()