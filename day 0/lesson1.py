from turtle import *


#we want to paint s house

#step 1:   draw a square
shape("turtle")
speed(1)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)       #height of the door
right(90)
forward(60)
right(90)
forward(100)       #height of the door
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(130, 50)
pendown()
                         #door handle                          
right(75)    
forward(1)


penup()
goto(130, 120)
pendown()

color("blue")
right(75)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)                #first window
forward(25)
right(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)




penup()
goto(70, 120)
pendown()

right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)                #secund window
forward(25)
right(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)




exitonclick()