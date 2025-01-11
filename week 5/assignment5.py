# Base class: Superhero
class Superhero:
    def __init__(self, name, power, team):
        self.name = name
        self.power = power
        self.team = team

    def display_info(self):
        print(f"Name: {self.name}, Power: {self.power}, Team: {self.team}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")
        
# Derived class: FlyingHero inherits from Superhero
class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.name} soars through the sky using {self.power}!")

# Derived class: Speedster inherits from Superhero
class Speedster(Superhero):
    def use_power(self):
        print(f"{self.name} speeds past enemies with {self.power}!")

# Create objects of each class
hero1 = Superhero("Iron Shield", "Super Strength", "Avengers")
hero2 = FlyingHero("Sky Falcon", "Wings", "Avengers")
hero3 = Speedster("Flashbolt", "Super Speed", "Justice League")

# Display info and use powers
hero1.display_info()
hero1.use_power()

hero2.display_info()
hero2.use_power()

hero3.display_info()
hero3.use_power()



#activity 2

# Base class: Vehicle
class Vehicle:
    def move(self):
        print("This vehicle is moving.")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road. 🚗")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky. ✈️")

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on water. 🚤")

# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Call the move() method for each vehicle
for vehicle in vehicles:
    vehicle.move()
