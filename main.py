class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def get_info(self):
        return f"Brand: {self.brand},Speed: {self.speed}"

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand,speed)
        self.doors = doors
    
    def get_info(self):
        return f"Brand: {self.brand},Speed: {self.speed},Doors: {self.doors}"

class Bike(Vehicle):
    def __init__(self, brand, speed, type):
        super().__init__(brand,speed)
        self.type =type
        
    def get_info(self):
        return f"Brand: {self.brand}, Speed: {self.speed}, Type: {self.type}"

# Create one object of each class and print their information
v = Vehicle('Generic', 50)
c = Car('Toyota', 120, 4)
b = Bike('Giant', 30, 'mountain')

print(v.get_info())
print(c.get_info())
print(b.get_info())