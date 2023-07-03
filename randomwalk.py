import turtle as t
import random
t.colormode(255)
R = 0
G = 0
B = 0
turtle_object1= t.Turtle()
turtle_object2= t.Turtle()
turtle_object1.width(5)
directions=[0,90, 180, 270]
turtle_object2.speed(100)
turtle_object1.speed(100)
for i in range(200):
    R = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    turtle_object1.color(R, G, B)
    num=random.randint(0,1)
    if(num==0):
        turtle_object1.left(90)
    else:
        turtle_object1.right(90)
    turtle_object1.forward(30)        
turtle_object2.width(5)
for i in range(200):
    R = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    turtle_object2.color(R, G, B)
    turtle_object2.setheading(random.choice(directions))
    turtle_object2.forward(30)

screen= t.Screen()
screen.exitonclick()