class Car:
    pass

car1 = Car()
car2 = Car()

print(type(car1)) 

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand      # attribute
        self.model = model      # attribute
        self.year = year        # attribute

# Create car objects
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.brand)   # Toyota
print(car1.model)   # Camry
print(car2.brand)   # Honda

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        self.is_running = True
        print(f"{self.brand} {self.model} started.")
    
    def stop(self):
        self.is_running = False
        print(f"{self.brand} {self.model} stopped.")
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
        status = "running" if self.is_running else "stopped"
        print(f"Status: {status}")

# Use the class
car = Car("Tesla", "Model 3", 2024)
car.display_info()
car.start()
car.display_info()
car.stop()
car.display_info()