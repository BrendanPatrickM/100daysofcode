import pandas
import turtle

IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title('U.S States Game')
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []
missed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States',
                                    prompt='Name a state.').title()
    if answer_state == 'Exit':
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        state_row = data[data.state == answer_state]
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(int(state_row.x), int(state_row.y))
        # item() vetches only the value
        tim.write(state_row.state.item())

for state in all_states:
    if state in guessed_states:
        pass
    else:
        missed_states.append(state)

missed_datafield = pandas.DataFrame(missed_states)
missed_datafield.to_csv('States_to_Learn.csv')
