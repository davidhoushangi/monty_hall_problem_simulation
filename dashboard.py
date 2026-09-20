import streamlit as st
from src.monty_hall_problem import monty_hall_game
import time

st.title(":zap: Monty Hall Simulation")
st.image("https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3f/Monty_open_door.svg/1280px-Monty_open_door.svg.png?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=thumbnail")
num_games = st.number_input(
    "Enter number of games to simulate",
    min_value=1, max_value=10000, 
    value=100
)

col1, col2 = st.columns(2)
col1.subheader('Win Percentage without Switching')
col2.subheader('Win Percentage with Switching')

chart1_placeholder = col1.empty()
chart2_placeholder = col2.empty()

if st.button("Run Simulation"):
    wins_no_switch = 0
    wins_switch = 0
    data_no_switch = []
    data_switch = []

    for i in range(num_games):
        if monty_hall_game(False):
            wins_no_switch += 1
        if monty_hall_game(True):
            wins_switch += 1

        data_no_switch.append(wins_no_switch / (i + 1))
        data_switch.append(wins_switch / (i + 1))

        chart1_placeholder.line_chart(data_no_switch)
        chart2_placeholder.line_chart(data_switch)

        time.sleep(0.01)
