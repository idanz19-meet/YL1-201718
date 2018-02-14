from turtle import Turtle
import turtle
import random
import time
import math

turtle.register_shape("gstq.gif")
turtle.register_shape("deutschland.gif")

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,shape,color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x, y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shapesize(r/10)
		self.shape(shape)
		self.color(color)
	def move(self, screen_width, screen_hieght):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		up_side_ball = new_y + self.r
		down_side_ball = new_y - self.r
		self.goto(new_x, new_y)
		if right_side_ball > (screen_width) or left_side_ball < (0):
			self.dx = -self.dx
			self.clear()
		if up_side_ball > (screen_hieght) or down_side_ball < -(screen_hieght):
			self.dy = -self.dy
			self.clear()

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.05
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)

NUMBER_OF_BALLS = 8
MINIMUM_BALL_RADIUS = 20
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
for i in range(NUMBER_OF_BALLS):
	x = random.randint(int(SCREEN_WIDTH-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while dx == 0:
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	while dy ==0:
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	n = randon.randit(0,1)
	s = 0
	if n = 0:
		s = "deutschland.gif"
	else:
		s = "deutschland.gif"
	sphere = Ball(x,y,dx,dy,radius,s,color)
	BALLS.append(sphere)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

while RUNNING:
	move_all_balls()
	turtle.getscreen().update()
	time.sleep(SLEEP)
turtle.mainloop()