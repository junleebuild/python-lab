###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram1, random
from turtle import Turtle, Screen, colormode

colormode(255)

color_list = colorgram1.rgb_colors

timmy = Turtle()
timmy.hideturtle()
timmy.penup()
x = -300
y = -300
timmy.goto(x, y)


for j in range(10):
    for i in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.forward(50)
    timmy.setheading(90)
    y+=50
    timmy.goto(x,y)
    timmy.setheading(0)



screen = Screen()
screen.exitonclick()






















