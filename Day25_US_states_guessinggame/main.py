import turtle
import pandas as pd

data = pd.read_csv('/Users/shivani/udemy_ds/python_projects/Day25_US_states_guessinggame/50_states.csv')
all_states = data['state'].to_list()
screen = turtle.Screen()
screen.title('U.S. States Game')
image = "/Users/shivani/udemy_ds/python_projects/Day25_US_states_guessinggame/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# #To the coordinates of the map

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# screen.mainloop()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    #Checking if state is in present in list or not
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #guess the state
        state_data = data[data['state'] == answer_state]
        t.goto(state_data['x'].item(), state_data['y'].item())
        t.write(answer_state)


