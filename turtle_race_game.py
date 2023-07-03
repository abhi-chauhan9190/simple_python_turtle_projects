import turtle as t
import random as r
sc=t.Screen()

all_turles=[]
sc.setup(500,400)
user_guess=sc.textinput(title="Make your guess" , prompt="Which turtle will win the race  Enter a color")

colorsa=["red" , "orange" , "blue" , "green" , "purple" , "black"]
y_indexes=[150 , 90 , 30 , -30 , -90 ,-150]
for i in range(0,6):
    t1=t.Turtle(shape="turtle")
    t1.color(colorsa[i])
    t1.penup()
    t1.goto(-230,y_indexes[i])
    all_turles.append(t1)

win=1
while win:
    for t in all_turles:
        
        if t.xcor() >= 220:
            winner=t.pencolor()
            print(f"winner is {winner}")
            if(winner==user_guess):
                print("You won !")
            else:
                print("You lose !")    
            
            win=0

        randd= r.randint(0,10)
        t.forward(randd)


sc.exitonclick()

