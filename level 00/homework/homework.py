from turtle import *

#we want to paint a house 

#step 1: draw a square 

width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door 

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door 
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

#drawing a roof 
color("purple")
right(150)
forward(200)
left(120)
forward(200)
#end of roof

penup()
goto(170, 170)
pendown()

#drawing windows
color("blue")
left(30)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

penup()
goto(30, 170)
pendown()

forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
#end of windows

exitonclick()