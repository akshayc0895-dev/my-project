# Step 3: Adding finally block

try:
    numerator = 10
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Calculation attempted.")