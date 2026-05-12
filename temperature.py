# Project 5: Celsius to Fahrenheit
# Temperature converter

print("=" * 35)
print("TEMPERATURE CONVERTER")
print("=" * 35)

# Show menu
print("\nWhat do you want to convert?")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Get choice
choice = input("\nEnter choice (1 or 2): ")

if choice == '1':
    # Celsius to Fahrenheit
    celsius = input("Enter temperature in Celsius: ")
    celsius = float(celsius)
    
    # Formula: (°C × 9/5) + 32 = °F
    fahrenheit = (celsius * 9/5) + 32
    
    print("\n" + "=" * 35)
    print("CONVERSION RESULT:")
    print("=" * 35)
    print(f"{celsius}°C = {fahrenheit}°F")
    
    # Bonus: Show common temperatures
    print("\n--- Reference ---")
    print(f"Water freezes: {fahrenheit}°F" if fahrenheit <= 32 else "")
    print(f"Water boils: {fahrenheit}°F" if fahrenheit >= 212 else "")
    print(f"Room temperature: {fahrenheit}°F" if 68 <= fahrenheit <= 77 else "")

elif choice == '2':
    # Fahrenheit to Celsius
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    fahrenheit = float(fahrenheit)
    
    # Formula: (°F - 32) × 5/9 = °C
    celsius = (fahrenheit - 32) * 5/9
    
    print("\n" + "=" * 35)
    print("CONVERSION RESULT:")
    print("=" * 35)
    print(f"{fahrenheit}°F = {celsius:.1f}°C")
    
    # Bonus: Show rounded version
    print(f"(Rounded: {celsius:.0f}°C)")

else:
    print("\nInvalid choice! Please select 1 or 2")

# Bonus: Show freezing and boiling points
print("\n" + "=" * 35)
print("DID YOU KNOW?")
print("=" * 35)
print("Water freezes at 0°C (32°F)")
print("Water boils at 100°C (212°F)")
print("Body temperature is 37°C (98.6°F)")

print("\n" + "=" * 35)