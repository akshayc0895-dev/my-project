# Project 4: Simple Calculator
# Add, subtract, multiply, divide two numbers

print("=" * 35)
print("SIMPLE CALCULATOR")
print("=" * 35)

# Get first number
num1 = input("Enter first number: ")
num1 = float(num1)  # Use float to allow decimals

# Get second number
num2 = input("Enter second number: ")
num2 = float(num2)

# Show menu of operations
print("\nChoose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# Get operation choice
choice = input("\nEnter choice (1/2/3/4): ")

# Perform calculation based on choice
print("\n" + "=" * 35)
print("RESULT:")
print("=" * 35)

if choice == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"{num1} × {num2} = {result}")

elif choice == '4':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} ÷ {num2} = {result}")
    else:
        print("ERROR: Cannot divide by zero!")

else:
    print("Invalid choice! Please select 1, 2, 3, or 4")

# Bonus: Show rounded result for division
if choice == '4' and num2 != 0:
    print(f"(Rounded: {result:.2f})")

print("\n" + "=" * 35)