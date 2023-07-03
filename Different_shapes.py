import turtle as t
import random
t.colormode(255)
R = 0
G = 0
B = 0
turtle_object1= t.Turtle()


for i in range(3,11):
    R = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    turtle_object1.color(R, G, B)

    for x in range(i):
        ang=360/i
        turtle_object1.forward(100)
        turtle_object1.left(ang)



screen= t.Screen()
screen.exitonclick()