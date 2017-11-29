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
	def __init__(self, size, colour, speed):
		Turtle.__init__(self)
#		self.home()
		self.hideturtle()
		self.penup()
		self.begin_poly()
		self.fd(size)
		self.left(60)
		self.fd(size)
		self.left(60)
		self.fd(size)
		self.left(60)
		self.fd(size)
		self.left(60)
		self.fd(size)
		self.left(60)
		self.fd(size)
		self.end_poly()
		p = self.get_poly()
		self.showturtle()
		register_shape("hexagon", p)
		self.shape("hexagon")
		self.color(colour)
		self.speed(speed)
	def Goaway(self, dis):
		self.fd(dis)

#hexy = Hexagon(30, "red", 8)
#hexy.Goaway(100)

class Polygon(Turtle):
	def __init__(self, lines):
		Turtle.__init__(self)
		self.hideturtle()
		self.penup()
		self.begin_poly()
		for i in range(lines):
			self.fd(20)
			self.left(360/lines)
		self.end_poly()
		p = self.get_poly()
		self.showturtle()
		register_shape("newshape", p)
		self.shape("newshape")
polygony = Polygon(30)


turtle.mainloop()
