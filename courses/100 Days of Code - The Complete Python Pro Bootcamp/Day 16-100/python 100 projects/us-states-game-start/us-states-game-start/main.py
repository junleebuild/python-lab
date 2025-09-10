import turtle
import pandas
import pandas as pd


def write_answer(answer, xcor, ycor):
    answer_turtle = turtle.Turtle()
    answer_turtle.hideturtle()
    answer_turtle.penup()
    answer_turtle.goto(xcor, ycor)
    answer_turtle.write(answer, align='center', font=("Arial", 10, "normal"))

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
count = 0
correct_guess = []
data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [ state for state in state_list if state not in correct_guess ]
        df = pd.DataFrame(missing_states, columns=["state"])
        df.to_csv("missing_states.csv")
        break
    if answer_state in state_list:
        x = int(data[data.state == answer_state]["x"].values[0])
        y = int(data[data.state == answer_state]["y"].values[0])
        write_answer(answer_state, x, y)
        correct_guess.append(answer_state)
        count += 1



screen.mainloop()