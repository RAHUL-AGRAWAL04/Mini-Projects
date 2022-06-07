#!/usr/bin/env python3
import turtle
from turtle import *
speed(5000)
bgcolor('black')
r,g,b=255,0,0
for i in range(int(255*3.5)):
	colormode(255)
	if i<255//3:
		g+=3
	elif i<255*2//3:
		r-=3
	elif i<255:
		b+=3
	elif i<255*4//3:
		g-=3
	elif i<255*5//3:
		r+=3
	else:
		b-=3
	fd(50+i)
	rt(91)
	try:
		pencolor(r,g,b)
	except:r,g,b=255,0,0
turtle.mainloop()
