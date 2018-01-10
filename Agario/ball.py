from turtle import Turtle
import turtle
import random
import time

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shapesize(r/10)
		self.shape("circle")
		self.color(color)
	def move(self, screen_width, screen_hieght):
		current_x = self.x
		new_x = current_x + self.dx
		current_y = self.y
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		up_side_ball = new_y + self.r
		down_side_ball = new_y - self.r
		if right_side_ball > (screen_width/2):
			new_x = current_x
		if left_side_ball < -(screen_width/2):
			new_x = current_x
		if up_side_ball > (screen_hieght/2):
			new_y = current_y
		if down_side_ball < -(screen_hieght/2):
			new_y = current_y
		self.goto(new_x, new_y)

player = Ball(0,0,40,100,30,"green")
player.penup()
player.move(200,200)
turtle.mainloop()