# Project 15: Coin Flip Simulator
# Simulate a random coin toss

import random

print("=" * 40)
print("COIN FLIP SIMULATOR")
print("=" * 40)

print("\n1. Flip once")
print("2. Flip multiple times")

choice = input("Enter choice (1 or 2): ")

if choice == '1':
    result = random.choice(["Heads", "Tails"])
    print(f"\nResult: {result}")

elif choice == '2':
    flips = int(input("How many flips? "))
    
    heads_count = 0
    tails_count = 0
    
    print("\nRESULTS:")
    for i in range(flips):
        result = random.choice(["Heads", "Tails"])
        print(f"Flip {i+1}: {result}")
        
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    
    print("\n" + "=" * 40)
    print("SUMMARY")
    print("=" * 40)
    print(f"Total flips: {flips}")
    print(f"Heads: {heads_count}")
    print(f"Tails: {tails_count}")
    print(f"Heads percentage: {(heads_count/flips)*100:.1f}%")
    print(f"Tails percentage: {(tails_count/flips)*100:.1f}%")

else:
    print("Invalid choice. Exiting.")

print("=" * 40)