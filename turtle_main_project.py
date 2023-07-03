import turtle as t
import random

# import colorgram
t.colormode(255)
R = 0
G = 0
B = 0
t1= t.Turtle()

# clrs=colorgram.extract('proimg.png',30)
clrs=[(235, 228, 211), (217, 218, 223), (104, 106, 125), (213, 152, 91), (140, 140, 150), (186, 62, 32), (225, 212, 109), (199, 147, 173), (237, 215, 225), (105, 112, 170), (177, 159, 47), (218, 224, 219), (186, 19, 9), (38, 40, 21), (27, 25, 63), (26, 42, 22), (223, 167, 194), (42, 44, 101), (205, 87, 58), (58, 68, 54), (132, 136, 132), (190, 187, 218), (230, 176, 172), (231, 65, 82)]
# rgbc=[]
# for c in clrs:
#     r=c.rgb.r
#     g=c.rgb.g
#     b=c.rgb.b
#     newc=(r,g,b)
#     rgbc.append(newc)
# print(rgbc)
# turtle_object1.speed(18)
# R = random.randrange(0, 257, 10)
# B = random.randrange(0, 257, 10)
# G = random.randrange(0, 257, 10)
# turtle_object1.color(R, G, B)
t1.speed(100)
t1.penup()
t1.setheading(225)
t1.forward(300)
t1.setheading(0)
# t1.pendown()
t1.hideturtle()
t1.speed(70)
for x in range(10):
    for i in range(10):
        t1.dot(15 , random.choice(clrs))
        t1.penup()
        t1.forward(50)
        # t1.pendown()
    t1.penup()    
    t1.setheading(90)
    t1.forward(50)
    t1.setheading(180)
    t1.forward(500)
    t1.setheading(0)
    # t1.pendown()    
screen= t.Screen()
screen.exitonclick()