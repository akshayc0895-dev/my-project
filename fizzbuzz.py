# Project 10: FizzBuzz

print("=" * 40)
print("FIZZBUZZ GAME")
print("=" * 40)

# Get the number from user
n = int(input("\nEnter a number: "))

print("\n" + "=" * 40)
print(f"FIZZBUZZ from 1 to {n}")
print("=" * 40)

for i in range(1, n + 1):

     # Check if divisible by both 3 and 5 (must come first!)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if divisible by 3
    elif i % 3 == 0:
        print("Fizz")
    # Check if divisible by 5
    elif i % 5 == 0:
        print("Buzz")
    # Otherwise, print the number
    else:
        print(i)
