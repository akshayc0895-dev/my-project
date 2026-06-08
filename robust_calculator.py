def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

print("Robust Calculator")
print("Operations: +, -, *, /")

while True:
    print("\n1. Calculate")
    print("2. Exit")
    choice = input("Enter choice: ")

    if choice == '2':
        print("Goodbye.")
        break
    elif choice == '1':
        try:
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")
            op = input("Operation (+, -, *, /): ")

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation.")
                continue

            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    else:
        print("Invalid choice.")