import streamlit as st
import random
from PIL import Image
st.title("My first app")

# --- Game Setup ---
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "guesses" not in st.session_state:
    st.session_state.guesses = 0

st.title("🎮 Guess the Number Game")
st.write("I'm thinking of a number between **1 and 100**. Can you guess it?")

# --- Image Upload ---
st.sidebar.header("🖼️ Upload your avatar!")
uploaded_image = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.sidebar.image(image, caption="Your Avatar", use_column_width=True)

# --- Game Logic ---
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
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.guesses = 0

