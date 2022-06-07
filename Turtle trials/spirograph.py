#!/usr/bin/env python3
import turtle
import time
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(100):
	for colours in ['red','magenta','blue','cyan','green','yellow','white']:
		turtle.color(colours)
		turtle.circle(150)
		turtle.left(20)
		time.sleep(0.1)
turtle.hideturtle()
