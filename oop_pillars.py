# The 4 Pillars of Object-Oriented Programming

print("=" * 50)
print("THE 4 PILLARS OF OOP")
print("=" * 50)

print("""
1. ENCAPSULATION
   - Bundling data and methods together
   - Hiding internal details (using _ or __)
   - Example: BankAccount hides transaction list

2. ABSTRACTION
   - Showing only essential features
   - Hiding complex implementation
   - Example: Car class hides how fuel consumption is calculated

3. INHERITANCE
   - Creating child classes from parent class
   - Reusing code
   - Example: SavingsAccount inherits from BankAccount

4. POLYMORPHISM
   - Same method name, different behavior
   - Example: Animal class with speak() - Dog barks, Cat meows
""")

# Simple inheritance example
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def honk(self):
        print("Beep beep!")

class Bike(Vehicle):
    def honk(self):
        print("Ring ring!")

class Truck(Vehicle):
    def honk(self):
        print("HOOOONK!")

# Polymorphism in action
vehicles = [Bike("Hero"), Truck("Volvo"), Vehicle("Generic")]

print("\nPolymorphism Example:")
for v in vehicles:
    print(f"{v.brand}: ", end="")
    v.honk()