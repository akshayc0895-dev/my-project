# Project 3: Even or Odd
# Check if a number is even or odd

print("=" * 30)
print("EVEN OR ODD CHECKER")
print("=" * 30)

#Ask for a number
number = input("Enter a whole number: ")

#conver to integer
number = int(number)

# check if even or odd using modulo operator (%)
# Even number divide by 2 with no remainder (remainder = 0)
# Odd numbers have remainder 1
if number % 2 == 0:
    print(f"\n{number} is EVEN!")
    print(f"Because {number} ÷ 2 = {number // 2} remainder 1")
    
# Bonus: Ask multiple numbers in a loop
print("\n--- BONUS: Try multiple numbers ---")
print("Type 'quit' to stop")

while True:
    user_input = input("\nEnter a number: ")
    if user_input == 'quit':
        print("Goodbye!")
        break
    
    num = int(user_input)
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")