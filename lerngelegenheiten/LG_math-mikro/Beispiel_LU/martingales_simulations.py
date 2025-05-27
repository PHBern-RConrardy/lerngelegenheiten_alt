import random

def roulette_simulation(starting_amount, rounds):
    total_amount = starting_amount
    original_bet = 1  # Starting bet amount
    current_bet = original_bet

    for round in range(rounds):
        # Simulate the bet outcome
        if random.random() < 0.5:  # 50% chance to lose
            total_amount -= current_bet  # Player loses the bet
            current_bet *= 2  # Double the bet for the next round
        else:  # 50% chance to win
            total_amount += current_bet  # Player wins the bet
            current_bet = original_bet  # Reset bet to the original amount

        # Check if the player has run out of money
        if total_amount <= 0:
            return True  # Player has run out of money

    return False  # Player did not run out of money

def simulate_games(num_games, starting_amount, rounds):
    run_out_count = 0

    for game in range(num_games):
        if roulette_simulation(starting_amount, rounds):
            run_out_count += 1  # Increment count if player runs out of money

    return run_out_count

# Set parameters for the simulation
num_games = 100  # Number of games to simulate
starting_amount = 100  # Starting with 100 CHF
rounds = 1000  # Number of rounds for each game

run_outs = simulate_games(num_games, starting_amount, rounds)
print(f"Out of money in {run_outs} out of {num_games} games.")
