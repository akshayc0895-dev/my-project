# Project 13: BMI Calculator
# Calculate Body Mass Index

print("=" * 40)
print("BMI CALCULATOR")
print("=" * 40)

print("\nChoose measurement system:")
print("1. Metric (kilograms, meters)")
print("2. Imperial (pounds, inches)")

choice = input("Enter choice (1 or 2): ")

if choice == '1':
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))
    bmi = weight / (height ** 2)
    
elif choice == '2':
    weight = float(input("Enter weight in pounds: "))
    height = float(input("Enter height in inches: "))
    bmi = (weight / (height ** 2)) * 703
    
else:
    print("Invalid choice. Exiting.")
    exit()

print("\n" + "=" * 40)
print("RESULTS")
print("=" * 40)
print(f"Weight: {weight}")
print(f"Height: {height}")
print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")
print("=" * 40)