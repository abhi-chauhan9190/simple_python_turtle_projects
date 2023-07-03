import turtle as t

t1 = t.Turtle()
sc= t.Screen()

t1.color("red")

def move_for():
    t1.forward(10)
def move_back():
    t1.backward(10)
def Leftr():
    t1.left(5)
def rightr():
    t1.right(5)  
def fclear():
    t1.clear() 
    t1.penup()
    t1.home()
    t1.pendown()
def fundo():
    t1.undo()    
sc.listen()
sc.onkey(key="Up",fun=move_for)
sc.onkey(key="Down",fun=move_back)
sc.onkey(key="Left",fun=Leftr)
sc.onkey(key="Right",fun=rightr)
sc.onkey(key="c",fun=fclear)
sc.onkey(key="u",fun=fundo)

sc.exitonclick()