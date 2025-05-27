import random

def roulette_simulation(starting_amount, rounds):
    total_amount = starting_amount
    original_bet = 1  # Starting bet amount
    current_bet = original_bet

    for round in range(rounds):
        # Simulate the bet outcome
        if random.random() < 0.5:  # 50% chance to lose
            total_amount -= current_bet  # Player loses the bet
            print(f"Round {round + 1}: You lost {current_bet} CHF! Current total: {total_amount} CHF")
            current_bet *= 2  # Double the bet for the next round
        else:  # 50% chance to win
            total_amount += current_bet  # Player wins the bet
            print(f"Round {round + 1}: You won {current_bet} CHF! Current total: {total_amount} CHF")
            current_bet = original_bet  # Reset bet to the original amount

        # Check if the player has run out of money
        if total_amount <= 0:
            print("You have run out of money!")
            break

    return total_amount

# Set initial amount and number of rounds
starting_amount = 100  # Starting with 100 CHF
rounds = 1000  # Number of rounds to simulate

final_amount = roulette_simulation(starting_amount, rounds)
print(f"Final amount after simulation: {final_amount} CHF")

