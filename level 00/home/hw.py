from turtle import *
#drawing a square
speed(20)
width(5)
color("pink")
begin_fill()
forward (200)
left(90)

forward(200)
left(90)

forward (200)
left(90)

forward(200)
left(90)
end_fill()

#drawing door
forward(70)
left(90)
color("purple")
begin_fill()
forward(90)  #height
right(90)
forward(60)
right(90)
forward(90)
end_fill()


#roof
penup()
goto(200 , 200)
right(150)

color("red")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()
#window n1
penup()
goto(175, 175)
pendown()

right(60)
color("blue")
begin_fill()
forward(45)
left(90)
forward(50)
left(90)
forward(45)
left(90)
forward(50)
end_fill()

color("brown")
penup()
goto(152, 124)
pendown()
forward(50)

penup()
goto(175, 150)
pendown()
left(90)
forward(45)


#window n2
penup()
goto(25, 175)
pendown()
right(180)
color("blue")
begin_fill()
forward(45)
right(90)
forward(50)
right(90)
forward(45)
right(90)
forward(50)
end_fill()


color("brown")
penup()
goto(45, 124)
pendown()
forward(50)

penup()
goto(70, 150)
pendown()
left(90)
forward(45)

exitonclick()