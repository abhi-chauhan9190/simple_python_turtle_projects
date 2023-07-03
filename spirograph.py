import turtle as t
import random
t.colormode(255)
R = 0
G = 0
B = 0
turtle_object1= t.Turtle()

turtle_object1.speed(18)

for i in range(100):
    R = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    turtle_object1.color(R, G, B)
    turtle_object1.circle(120)
    turtle_object1.right(5)



screen= t.Screen()
screen.exitonclick()