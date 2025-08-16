import streamlit as st
import random
st.title("My first app")


# Set up session state for score
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "ai_score" not in st.session_state:
    st.session_state.ai_score = 0

st.title("✊✋✌️ Rock, Paper, Scissors")

# Choices
choices = ["Rock", "Paper", "Scissors"]
emoji_map = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

st.write("Choose your move:")

# Create buttons
col1, col2, col3 = st.columns(3)
user_choice = None

with col1:
    if st.button("✊ Rock"):
        user_choice = "Rock"
with col2:
    if st.button("✋ Paper"):
        user_choice = "Paper"
with col3:
    if st.button("✌️ Scissors"):
        user_choice = "Scissors"

# Game logic
def determine_winner(user, ai):
    if user == ai:
        return "draw"
    elif (
        (user == "Rock" and ai == "Scissors") or
        (user == "Paper" and ai == "Rock") or
        (user == "Scissors" and ai == "Paper")
    ):
        return "user"
    else:
        return "ai"

if user_choice:
    ai_choice = random.choice(choices)
    st.write(f"You chose: {emoji_map[user_choice]} **{user_choice}**")
    st.write(f"AI chose: {emoji_map[ai_choice]} **{ai_choice}**")

    winner = determine_winner(user_choice, ai_choice)

    if winner == "draw":
        st.info("🤝 It's a draw!")
    elif winner == "user":
        st.success("🎉 You win!")
        st.session_state.user_score += 1
    else:
        st.error("😢 You lose!")
        st.session_state.ai_score += 1

    # Show scores
    st.markdown("---")
    st.subheader("📊 Scoreboard")
    st.write(f"**You**: {st.session_state.user_score}")
    st.write(f"**AI**: {st.session_state.ai_score}")


