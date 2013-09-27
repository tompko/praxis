import random

def game():
    winning_door = random.choice([1,2,3])
    chosen_door = random.choice([1,2,3])

    return chosen_door != winning_door

def simulate(num_games):
    stick, switch = 0, 0

    for i in range(num_games):
        if game():
            switch += 1
        else:
            stick += 1

    return float(stick) / num_games, float(switch) / num_games

print simulate(100000)
