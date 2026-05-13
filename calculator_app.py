# Calculator App
# Perform addition, subtraction, multiplication, and division

print("=" * 40)
print("CALCULATOR APP")
print("=" * 40)

while True:
    print("\n" + "-" * 40)
    print("MENU:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("-" * 40)
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("Goodbye!")
        break
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select 1-5.")
        continue
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("\n" + "=" * 40)
    print("RESULT")
    print("=" * 40)
    
    if choice == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    
    elif choice == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    
    elif choice == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    
    print("=" * 40)

print("=" * 40)