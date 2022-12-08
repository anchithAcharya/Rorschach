from util import *
from digits import Digit
from PIL import ImageColor, Image
from point import Point, autocast_point


class Cursor:
	class Direction():
		UP    = Point(0,-1)
		DOWN  = Point(0,1)
		LEFT  = Point(-1,0)
		RIGHT = Point(1,0)

		# START = ('-', '-')
		# END = ('+', '+')

		# ROW_START = ('-', 0)
		# ROW_END = ('+', 0)
		# COL_START = (0, '-')
		# COL_END = (0, '+')

	@autocast_point
	def __init__(self, image: Image):
		self.pos = Point(0,0)
		self.image_dim = Point(*image._size)
		self.image_center = Point(*((x//2) for x in self.image_dim))
		self.image: Image = image
		self.Xsymmetry = False

	@autocast_point
	def point(self, to: Point):
		if to in Point.range(self.image_dim):
			self.pos = to

		else: raise ValueError(f"Cannot point cursor at {to} (Out of bounds: {Point(0,0)} to {self.image_dim})")

	@autocast_point
	def move(self, direction: Point):
		new_pos = self.pos + direction
		try:
			self.point(new_pos)

		except ValueError: raise ValueError(f"Cannot move cursor to {new_pos} (Out of bounds: {Point(0,0)} to {self.image_dim})")

	def draw_dot(self, advance = True, color="black"):
		self.image.putpixel(self.pos, ImageColor.getcolor(color, IMAGE_MODE))

		if self.Xsymmetry:
			inv_x = self.image_center.x + (self.image_center.x - self.pos.x)
			self.image.putpixel((inv_x, self.pos.y), ImageColor.getcolor(color, IMAGE_MODE))

		if advance: self.move(Point.Direction.RIGHT)

	@autocast_point
	def draw_box(self, pointA: Point, pointB: Point = None, relative = False, color="black"):
		pointB = pointB or self.pos

		if pointA.x > pointB.x: pointA.x, pointB.x = pointB.x, pointA.x
		if pointA.y > pointB.y: pointA.y, pointB.y = pointB.y, pointA.y

		pointB = pointB+Point(1,1)

		if relative:
			pointA = self.pos + pointA
			pointB = self.pos + pointB

		for x,y in Point.range(pointA, pointB):
			self.point((x,y))
			self.draw_dot(advance=False, color=color)

	def draw_digit(self, digit: Digit, color="black"):
		start_pos = self.pos

		for instruction in digit.draw_instructions:
			self.draw_box(instruction[0], instruction[1], relative = True, color=color)
			self.point(start_pos)
		self.point((start_pos.x+digit.width, start_pos.y))

# a = Cursor.Direction.UP.value + Cursor.Direction.LEFT.value
# b = (2,3) + Cursor.Direction.RIGHT.value
# c = (2,3) + Cursor.Direction.START.value