from turtle import
import random
import math

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
def ball_coll(ball_1,ball_2):
	if (ball_2.radius + ball_1.radius) > (math.sqrt(math.pow(ball_1.xcor - ball_2.xcor,2)+(math.pow(ball_1.ycor - ball_2.ycor)))
		ball_1.fd(100)
		ball_2.left(180)
		ball_2.fd(100)

Timmy = Ball(20,"red",2)
Tommy = Ball(10,"green",4)
