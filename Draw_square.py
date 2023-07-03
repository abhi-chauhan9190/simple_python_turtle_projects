from turtle import Turtle,Screen

turtle_object1= Turtle()

turtle_object1.color("blue")

for i in range(0,4):
    turtle_object1.forward(100)
    turtle_object1.left(90)


"""turtle_object1.forward(100)
turtle_object1.left(90)
turtle_object1.forward(100)
turtle_object1.left(90)
turtle_object1.forward(100)
turtle_object1.left(90)
turtle_object1.forward(100)"""



screen= Screen()
screen.exitonclick()