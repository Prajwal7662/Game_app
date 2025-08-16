import numpy as np
a = np.array([1,2,3,4,5])
print(a)

import streamlit as st
st.title("My first app")


import streamlit as st
import random

# Set a session state for the number to guess
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "guesses" not in st.session_state:
    st.session_state.guesses = 0

st.title("🎮 Guess the Number Game")
st.write("I'm thinking of a number between **1 and 100**. Can you guess it?")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    st.session_state.guesses += 1
    if guess < st.session_state.number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Correct! The number was {st.session_state.number}.")
        st.balloons()
        st.write(f"You guessed it in {st.session_state.guesses} tries!")
        # Reset the game
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.guesses = 0

