import random

class Dog:
    def __init__(self, name="Bobik", breed="German Shepherd"):
        self.name = name
        self.breed = breed
        self.energy = 200
        self.hunger = 100
        self.happiness = 50

    def play(self):
        print(f"{self.name} Playing")
        self.energy -= 10
        self.hunger -= 5
        self.happiness += 10

    def feed(self):
        print(f"{self.name} Eating")
        self.hunger += 20

    def the_urge_to_poop_in_a_slipper(self):
        print(f"{self.name} Pooping")
        self.happiness += 50

    def the_urge_to_poop_in_a_slipper(self):
            print(f"{self.name} Pooping")
            self.energy += 20

    def status(self):
        print(f"{self.name}'s Status:")
        print(f"Breed: {self.breed}")
        print(f"Energy: {self.energy}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")

