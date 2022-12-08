from util import *

class Digit:
	atlas = {}

	def __init__(self, digit, width, draw_instructions):
		self.digit = digit
		self.width = width
		self.draw_instructions = draw_instructions

	def __repr__(self):
		return self.digit

Digit.atlas = {
	0 : Digit('0', 4,
		(
			((0,0), (2,1)),
			((0,2), (0,4)),
			((2,2), (2,4)),
			((0,5), (2,6)),
		)
	),

	1 : Digit('1', 2,
		(
			((0,0), (0,6)),
		)
	),

	2 : Digit('2', 4,
		(
			((-1,0), (2,0)),
			((2,0), (2,3)),
			((2,3), (0,3)),
			((0,3), (0,6)),
			((0,6), (3,6)),
		)
	),

	3 : Digit('3', 4,
		(
			((0,0), (2,0)),
			((2,0), (2,6)),
			((-1,3), (3,3)),
			((0,6), (2,6)),
		)
	),

	4 : Digit('4', 4,
		(
			((0,0), (0,3)),
			((2,0), (2,6)),
			((0,3), (2,3)),
		)
	),

	5 : Digit('5', 4,
		(
			((0,0), (3,0)),
			((0,0), (0,3)),
			((2,3), (0,3)),
			((2,3), (2,6)),
			((-1,6), (2,6)),
		)
	),

	6 : Digit('6', 4,
		(
			((0,0), (3,0)),
			((0,0), (0,6)),
			((1,2), (2,6)),
		)
	),

	7 : Digit('7', 4,
		(
			((0,0), (2,0)),
			((2,0), (2,6)),
			((-1,3), (3,3)),
		)
	),

	8 : Digit('8', 4,
		(
			((0,0), (2,6)),
		)
	),

	9 : Digit('9', 4,
		(
			((2,0), (2,6)),
			((0,0), (1,4)),
			((-1,6), (2,6)),
		)
	),
}