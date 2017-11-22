from turtle import *
colormode(255)
import turtle

class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
#squary = Square(5)

class Hexagon(Turtle):
	def __init__(self, size):
		turtle.begin_poly()
		turtle.fd(10)
		turtle.left(60)
		turtle.fd(10)
		turtle.left(60)
		turtle.fd(10)
		turtle.left(60)
		turtle.fd(10)
		turtle.left(60)
		turtle.fd(10)
		turtle.end_poly()
		p = turtle.get_poly()
		register_shape("hexagon", p)
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("hexagon")
hexy = Hexagon(10)

turtle.mainloop()
