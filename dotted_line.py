from turtle import Turtle,Screen
turtle_object1= Turtle()
turtle_object1.color("blue")


for i in range(15):
    turtle_object1.forward(10)
    turtle_object1.penup()
    turtle_object1.forward(10)
    turtle_object1.pendown()

screen= Screen()
screen.exitonclick()