from turtle import Turtle,Screen
import random
global timmy
is_race_on=False
screen=Screen()
colors=["red","pink","purple","orange","blue"]
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
y_positions=[50,30,10,-10,-30,-50]
all_turtles=[]
for turtle_index in range(0,5):

    timmy = Turtle("turtle")
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(timmy)
if  user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:

            winning_turtlecolour=turtle.pencolor()
            if winning_turtlecolour==user_bet:

                print(f"You've Won!! The {winning_turtlecolour} turtle is the winner.")
            else:
                print(f"You've lost!! The {winning_turtlecolour} turtle is the winner.")
            is_race_on=False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()