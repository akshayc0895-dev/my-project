# Project 8: Multiplication table
# Print the multiplication table for any number

print("=" * 40)
print("MULTIPLICATION TABLE GENERATOR")
print("=" * 40)


# Get the number from user
number = int(input("\nEnter a number: "))

# Get range
print("\nChoose range:")
print("1. Default (1 to 10)")
print("2. Custom range")

choice = input("Enter choice (1 or 2): ")

print("\n" + "=" * 40)
print(f"MULTIPLICATION TABLE FOR {number}")
print("=" * 40)

if choice == '1':

    for i in range(1, 11):
        result = number * i
        print(f"{number} × {i:2} = {result:3}")
        
elif choice == '2':
    # Custom range
    start = int(input("Start from: "))
    end = int(input("Go up to: "))

    print("\n" + "-" * 40)
    for i in range(start, end + 1):
        result = number * i
        print(f"{number} × {i:2} = {result:3}")

else:
    print("Invalid choice! Showing default (1 to 10)")
    for i in range(1, 11):
        result = number * i
        print(f"{number} × {i:2} = {result:3}")