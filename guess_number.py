# Project 9, Guess the number, Random number guessing game.

import random

print("=" * 40)
print("GUESS THE NUMBER GAME")
print("=" * 40)

# setting the range
lowest = 1
highest = 100

# Generate random number
secret_number = random.randint(lowest, highest)

print(f"\nI'm thinking of a number between {lowest} and {highest}")
print("Can you guess what it is?")

# variables
attempts = 0
max_attempts = 10
guessed_correctly = False

# Main game loop
while attempts < max_attempts:
    guess = input(f"\nAttempt {attempts + 1}/{max_attempts} - Your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < lowest or guess > highest:
        print(f"Please guess between {lowest} and {highest}!")

    elif guess < secret_number:
        print("Too low! Try a higher number.")

    elif guess > secret_number:
        print("Too high! Try a lower number.")

    else:
        print(f"\n CORRECT! ")
        print(f"You guessed it in {attempts} attempts!")
        guessed_correctly = True
        break

# After the loop ends (either win or lose)
if not guessed_correctly:
    print(f"\n Out of attempts! The number was {secret_number}.")
    print("Better luck next time!")

print("\n" + "=" * 40)
print("GAME STATISTICS")
print("=" * 40)
print(f"Secret number: {secret_number}")
print(f"Total attempts used: {attempts}")
print(f"Max attempts allowed: {max_attempts}")

play_again = input("\nPlay again? (yes/no): ").lower()
if play_again == 'yes' or play_again == 'y':
    print("\n" + "=" * 40)
    print("RESTARTING GAME...")
    print("=" * 40)
    print("Run the program again to play!")
else:
    print("\nThanks for playing! Goodbye!")

print("=" * 40)