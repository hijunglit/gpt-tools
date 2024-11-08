class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

class GuardDog(Dog):

    def rrrr(self):
        print("Stay away!")

class Puppy(Dog):
    def woof_woof(self):
        print("woof woof!")
