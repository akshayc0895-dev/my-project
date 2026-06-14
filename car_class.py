# Car Class with multiple attributes and methods

class Car:
    def __init__(self, brand, model, year, color, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0
        self.is_running = False
        self.speed = 0
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} started.")
        else:
            print("Car is already running.")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print(f"{self.brand} {self.model} stopped.")
        else:
            print("Car is already stopped.")
    
    def refuel(self, amount):
        """Add fuel to the car"""
        if amount <= 0:
            raise ValueError("Fuel amount must be positive")
        if self.fuel_level + amount > self.fuel_capacity:
            print(f"Can only add {self.fuel_capacity - self.fuel_level} liters.")
            self.fuel_level = self.fuel_capacity
        else:
            self.fuel_level += amount
        print(f"Fuel level: {self.fuel_level}/{self.fuel_capacity} L")
    
    def accelerate(self, increase):
        """Increase speed"""
        if not self.is_running:
            print("Start the car first!")
            return
        if self.fuel_level <= 0:
            print("Out of fuel! Cannot accelerate.")
            return
        self.speed += increase
        self.fuel_level -= increase * 0.1  # Fuel consumption
        if self.fuel_level < 0:
            self.fuel_level = 0
        print(f"Speed: {self.speed} km/h | Fuel: {self.fuel_level:.1f} L")
    
    def brake(self, decrease):
        """Decrease speed"""
        self.speed = max(0, self.speed - decrease)
        print(f"Speed: {self.speed} km/h")
    
    def display_info(self):
        """Display all car information"""
        print("\n" + "=" * 40)
        print(f"CAR INFORMATION")
        print("=" * 40)
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Fuel: {self.fuel_level}/{self.fuel_capacity} L")
        print(f"Status: {'Running' if self.is_running else 'Stopped'}")
        print(f"Speed: {self.speed} km/h")
        print("=" * 40)

# Test the Car class
if __name__ == "__main__":
    my_car = Car("Honda", "Civic", 2023, "Red", 50)
    my_car.display_info()
    
    my_car.refuel(30)
    my_car.start()
    my_car.accelerate(40)
    my_car.accelerate(20)
    my_car.brake(30)
    my_car.stop()
    my_car.display_info()