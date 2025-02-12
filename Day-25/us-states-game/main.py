from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.colormode(255)
screen.title("U.S. State Game")
screen.setup(width=700, height=450)
screen.bgpic("blank_states_img.gif")

# read csv file
data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

guessed_state = []

score = 0
while score < 50:
    user_input = screen.textinput(title=f"{score}/50", prompt="Enter State names: ").title()
    if user_input in states:
        guessed_state.append(user_input)
        t = Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == user_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_input, align="center", font=("Courier", 10, "normal"))
        score += 1
    elif user_input == "Exit":
        # save missing states
        missing_state = [state for state in states if state not in guessed_state]
        break

screen.exitonclick()
