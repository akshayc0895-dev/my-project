try:
    num = int(input("Enter a number: "))
    print(f"You entered {num}")
except ValueError:
    print("That's not a valid number!")
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Execution finished.")
try:
    with open("test.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Creating a new one.")
    with open("test.txt", "w") as file:
        file.write("Default content")
def set_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
    print(f"Age set to {age}")

try:
    set_age(150)
except ValueError as e:
    print(f"Error: {e}")