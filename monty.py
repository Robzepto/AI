import random

def monty_hall_simulation(switch=False):

    prize_door = random.randint(1, 3)

    contestant_choice = random.randint(1, 3)

    remaining_doors = [door for door in [1, 2, 3] if door != contestant_choice and door != prize_door]
    door_revealed = random.choice(remaining_doors)

    print(f"Contestant picks door {contestant_choice}")
    print(f"Host reveals door {door_revealed}")
    
    if switch:
        
        new_choice = [door for door in [1, 2, 3] if door != contestant_choice and door != door_revealed][0]
        contestant_choice = new_choice

    win = contestant_choice == prize_door
    
    print("Contestant wins!" if win else "Contestant loses.")

    
    return win

num_simulations = 10
switch_wins = 0
stay_wins = 0

for _ in range(num_simulations):
    switch_wins += monty_hall_simulation(switch=True)
    stay_wins += monty_hall_simulation()

switch_win_percentage = (switch_wins / num_simulations) * 100
stay_win_percentage = (stay_wins / num_simulations) * 100

print(f"Win percentage if switching doors: {switch_win_percentage:.2f}%")
print(f"Win percentage if staying with initial choice: {stay_win_percentage:.2f}%")
