from util import *
import tkinter as tk
from PIL import Image, ImageTk
from point import Point
from cursor import Cursor
from digits import Digit

def drawNumber(number):
	im = Image.new(IMAGE_MODE, (110, 110), "white")
	c = Cursor(im)

	# c.draw_box(Point(c.image_center.x, 0), Point(c.image_center.x, c.image_dim.y-1), color="red")
	# c.Xsymmetry = True

	c.point((25,50))

	for digit in str(int(number)):
		c.draw_digit(Digit.atlas[int(digit)])

	return im


number = 0
def update_number(delta):
	global number, label, imgTK
	number += (delta/120)

	if number < 0: number = 0
	elif number > 60: number = 60

	image = drawNumber(number)
	imgTK = ImageTk.PhotoImage(image.resize(imgHeight, resample=Image.NEAREST))

	label.configure(image=imgTK)

root = tk.Tk()
root.geometry("600x600+800+100")
root.resizable(False, False)

root.update()
imgHeight = (root.winfo_width(), root.winfo_height())

image = drawNumber(number)
imgTK = ImageTk.PhotoImage(image.resize(imgHeight, resample=Image.NEAREST))

label = tk.Label(root, image=imgTK)
label.pack(expand=True, fill="both")
label.bind("<MouseWheel>", lambda e: update_number(e.delta))

root.mainloop()