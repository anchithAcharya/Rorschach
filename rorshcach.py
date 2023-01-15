from util import *
import tkinter as tk
from PIL import Image, ImageTk
from point import Point
from cursor import Cursor
from digits import Digit

def drawImage(hours, minutes):
	im = Image.new(IMAGE_MODE, (110, 110), "white")
	c = Cursor(im)

	# c.draw_box(Point(c.image_center.x, 0), Point(c.image_center.x, c.image_dim.y-1), color="red")
	c.Xsymmetry = True

	c.point((c.image_center.x+1,50))

	hours = str(int(hours))
	if len(hours) == 1: hours = '0' + hours

	minutes = str(int(minutes))
	if len(minutes) == 1: minutes = '0' + minutes

	for digit in hours:
		c.draw_digit(Digit.atlas[digit])

	offset = sum([Digit.atlas[digit].width for digit in minutes])
	c.point((c.image_center.x-offset+1,57))

	for digit in minutes:
		c.draw_digit(Digit.atlas[digit])

	return im


hours = 0
minutes = 0

def update_time(e):
	global hours, minutes, label, imgTK

	if e.y < 300:
		hours += (e.delta/120)

		if hours < 0: hours = 0
		elif hours > 60: hours = 60

	else:
		minutes += (e.delta/120)

		if minutes < 0: minutes = 0
		elif minutes > 60: minutes = 60

	image = drawImage(hours, minutes)
	imgTK = ImageTk.PhotoImage(image.resize(imgHeight, resample=Image.NEAREST))

	label.configure(image=imgTK)

root = tk.Tk()
root.geometry("600x600+800+100")
root.resizable(False, False)

root.update()
imgHeight = (root.winfo_width(), root.winfo_height())

image = drawImage(hours, minutes)
imgTK = ImageTk.PhotoImage(image.resize(imgHeight, resample=Image.NEAREST))

label = tk.Label(root, image=imgTK)
label.pack(expand=True, fill="both")
label.bind("<MouseWheel>", lambda e: update_time(e))

root.mainloop()