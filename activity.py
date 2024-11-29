class Mover:
    def move(self):
        pass

class Dog(Mover):
    def move(self):
        print("Running 🐕")

class Bird(Mover):
    def move(self):
        print("Flying 🐦")

class Car(Mover):
    def move(self):
        print("Driving 🚗")

class Plane(Mover):
    def move(self):
        print("Flying ✈️")

# List of movers
movers = [Dog(), Bird(), Car(), Plane()]

# Iterate through the list and call the move method
for mover in movers:
    mover.move()
