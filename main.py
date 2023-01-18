
import turtle

import pandas


screen = turtle.Screen()
screen.title("US States Game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_details = pandas.read_csv("50_states.csv")
state_names = state_details["state"].to_list()



max_states = 50
states_guessed = []



while len(states_guessed) < max_states:
    
    user_guess = screen.textinput(title=f"{len(states_guessed)} / {max_states} ", prompt="Guess a US state..").title()
    if user_guess in state_names and not user_guess in states_guessed:
        states_guessed.append(user_guess)
        state_x = int(state_details[state_details.state == user_guess].x)
        state_y = int(state_details[state_details.state == user_guess].y)
        state = turtle.Turtle()
        state.up()
        state.hideturtle()
        state.goto(state_x,state_y)
        state.write(f"{user_guess}", align= "Center", font=("arial", 5, "bold"))
    elif user_guess not in state_names:        
        print ("no good!")
    elif user_guess in states_guessed:
        print ("already guessed !")





turtle.mainloop()