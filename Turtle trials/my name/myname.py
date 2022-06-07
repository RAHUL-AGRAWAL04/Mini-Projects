#Python Turtle - WordArt Challenge - www.101computing.net/python-turtle-wordart-challenge/
import turtle
from turtle import *
import random
from alphabet import alphabet
from turtle import Turtle, Screen
import time


myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
window = turtle.Screen()
window.setup(1300,1000)
window.bgcolor("#000000")
myPen.pensize(5)

def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown()
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing 
    time.sleep(0.1)
    

#Main Program Starts Here
fontSize = 50
characterSpacing = 5
fontColor = "#FF00FF"

message = "RAHUL"
displayMessage(message,fontSize,fontColor,-500,0)
wn = Screen()
wn.mainloop()
