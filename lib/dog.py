#!/usr/bin/env python3

# List of approved dog breeds
APPROVED_BREEDS = [
    "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", 
    "French Bulldog", "Pug", "Pointer"
]

class Dog:
    def __init__(self, name="Bosco", breed="Corgi"):
        # Set initial values for name and breed
        self.name = name
        self.breed = breed

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name with validation
    def set_name(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()

    # Property for name
    name = property(get_name, set_name)

    # Getter for breed
    def get_breed(self):
        return self._breed

    # Setter for breed with validation
    def set_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    # Property for breed
    breed = property(get_breed, set_breed)



