from turtle import Turtle
import turtle
import random
import time

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x, y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shapesize(r/10)
		self.shape("circle")
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
		if right_side_ball > (screen_width) or left_side_ball < -(screen_width):
			self.dx = -self.dx
			self.clear()
		if up_side_ball > (screen_hieght) or down_side_ball < -(screen_hieght):
			self.dy = -self.dy
			self.clear()
		#self.goto(new_x, new_y)
