from turtle import Turtle
import turtle
import random
import time
import math
from ball.py import Ball

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

my_ball = Ball(0,0,40,100,30,"green")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
for i in NUMBER_OF_BALLS:
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH + MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.randint(0,225), random.randint(0,225),random.randint(0,225))
	sphere = Ball(x,y,dx,dy,radius,color)
	BALLS.append(sphere)

for i in BALLS:
	i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a, ball_b):
	if ball_a.r == ball_b.r and ball_a.xcor == ball_b.xcor and ball_a.ycor == ball_b.ycor:
		return False
	else if math.sqrt(math.pow((ball_a.xcor - ball_b.xcor),2) + math.pow((ball_a.ycor - ball_b.ycor),2))+10 < ball_a.r + ball_b.r:
		return True
	else:
		return False
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a, ball_b):
				r_of_ball_a = ball_a.r
				r_of_ball_b = ball_b.r
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH + MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS)
				x_axis = 0
				while x_axis == 0:
					x_axis = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				y_axis = 0
				while y_axis == 0:
					y_axis = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color = (random.randint(0,225), random.randint(0,225),random.randint(0,225))
				if r_of_ball_a < r_of_ball_b:
					ball_a.goto(x,y)
					ball_a.dx = x_axis
					ball_a.dy = y_axis
					ball_a.r = radius
					ball_a.shapesize(ball_a.r/10)
					ball_a.color(color)
					ball_b.r += 1
					ball_b.shapesize(ball_b.r/10)
				else:
					ball_b.goto(x,y)
					ball_b.dx = x_axis
					ball_b.dy = y_axis
					ball_b.r = radius
					ball_b.shapesize(ball_a.r/10)
					ball_b.color(color)
					ball_a.r += 1
					ball_a.shapesize(ball_b.r/10)
#Holy mother of Jesus... that was complex
