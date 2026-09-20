import random

def monty_hall_game(switch_doors):
    """_summary_

    Args:
        switch_doors (_bool_): user add True to swith the door and False to keep the initial choice

    Returns:
        _bool_: True is the door has a car behind it nad False if there is a goat behind the door
    """
    doors = ["car", "goat", "goat"]
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    if switch_doors:
        door_revealed = [i for i in range(3) if i != initial_choice and doors[i] != "car"]
        door_revealed = random.choice(door_revealed)
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == "car"


def simulate_game(num_games):
    """Calculates the % of winning and loosing when player choose to swith teh door or keep the initial choice

    Args:
        num_games (_int_): user adds the number of games in interger
    """
    num_wins_witout_switching = sum([monty_hall_game(False) for _ in range(num_games)])
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(num_games)])

    print(f"Lossing % : {num_wins_witout_switching / num_games}, Winning % : {num_wins_with_switching / num_games}")


if __name__ == "__main__:
  simulate_game(100_000)
