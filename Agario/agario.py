from turtle import Turtle
import turtle
import random
import time
import math
from ball import Ball
import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("meansofproduction.mp3")

sound.play()
#import pyglet

#music = pyglet.resource.media('meansofproduction.mp3')
#music.play()

#pyglet.app.run()

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.05
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)

my_ball = Ball(0,0,0,0,30,"green")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
for i in range(NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while dx == 0:
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	while dy ==0:
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	sphere = Ball(x,y,dx,dy,radius,color)
	BALLS.append(sphere)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	dist = math.sqrt(math.pow(ball_a.xcor() - ball_b.xcor(),2) + math.pow(ball_a.ycor() - ball_b.ycor(),2))
	if dist+10 < ball_a.r + ball_b.r:
		return True
	return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a, ball_b):
				r_of_ball_a = ball_a.r
				r_of_ball_b = ball_b.r
				x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				x_axis = 0
				while x_axis == 0:
					x_axis = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				y_axis = 0
				while y_axis == 0:
					y_axis = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color = (random.random(), random.random(), random.random())
				if r_of_ball_a < r_of_ball_b:
					ball_a.goto(x, y)
					ball_a.dx = x_axis
					ball_a.dy = y_axis
					ball_a.r = radius
					ball_a.shapesize(ball_a.r/10)
					ball_a.color(color)
					ball_b.r += 1
					ball_b.shapesize(ball_b.r/10)
				else:
					ball_b.goto(x, y)
					ball_b.dx = x_axis
					ball_b.dy = y_axis
					ball_b.r = radius
					ball_b.shapesize(ball_b.r/10)
					ball_b.color(color)
					ball_a.r += 1
					ball_a.shapesize(ball_a.r/10)

def check_myball_collision():
	for i in BALLS:
		if collide(my_ball,i):
			my_ball_radius = my_ball.r
			other_ball_radius = i.r
			x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
			y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
			x_axis = 0
			while x_axis == 0:
				x_axis = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			y_axis = 0
			while y_axis == 0:
				y_axis = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
			radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
			color = (random.random(), random.random(), random.random())
			if my_ball_radius > other_ball_radius:
				i.goto(x, y)
				i.dx = x_axis
				i.dy = y_axis
				i.r = radius
				i.shapesize(i.r/10)
				i.color(color)
				my_ball.r += 0.5
				my_ball.shapesize(my_ball.r/10)
			else:
				return False	
	return True

def movearound(event):
	my_ball.goto(event.x - SCREEN_HEIGHT, SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()

not_yet_in_level_2 = True

while RUNNING:
	# if (SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2) or (SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2):
	# 	SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	# 	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	#for i in BALLS:
	#	i.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	move_all_balls()
	check_all_balls_collision()
	# my_ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	if my_ball.r > 45 and not_yet_in_level_2:
		MINIMUM_BALL_RADIUS = 15
		MAXIMUM_BALL_RADIUS = 50
		MINIMUM_BALL_DX = -1
		MAXIMUM_BALL_DX = 10
		MINIMUM_BALL_DY = -1
		MAXIMUM_BALL_DY = 10
		not_yet_in_level_2 = False
	RUNNING = check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)

#Don't give up!
turtle.mainloop()