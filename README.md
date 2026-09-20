# Monty Hall Simulation Dashboard
<img width="250" height="154" alt="image" src="https://github.com/user-attachments/assets/64829c0a-1107-42ed-85fa-8c035b637d11" />



An interactive web application built with **Streamlit** that simulates the famous **Monty Hall problem**. This project demonstrates the counter-intuitive mathematical advantage of switching doors over staying with your initial choice.

## The Monty Hall Problem

In the Monty Hall problem, you are presented with three doors:
*   Behind one door is a **car** (you win).
*   Behind the other two doors are **goats** (you lose).

You pick a door. The host (Monty Hall), who knows what is behind each door, opens one of the other two doors to reveal a goat. You are then given the choice to either **stick with your original choice** or **switch to the remaining unopened door**.

**The Counter-Intuitive Math:**
*   If you stay: You have a **33.3%** chance of winning.
*   If you switch: You have a **66.6%** chance of winning.

This application visually proves this mathematical fact by simulating thousands of games and dynamically plotting the running win percentages.

## Project Structure

```text
Monty/
├── dashboard.py               # The Streamlit web application
└── src/
    ├── __init__.py            # Makes 'src' a Python package
    └── monty_hall_problem.py  # Core simulation logic
```

## Dashboard
<img width="771" height="605" alt="image" src="https://github.com/user-attachments/assets/195d23f9-26db-4031-b970-074ade54e56a" />

