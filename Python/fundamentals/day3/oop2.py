class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="dog")

    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="cat")

    def make_sound(self):
        print("Meow")




my_dog = Dog("Fido")
my_cat = Cat("Whiskers")

print(my_dog.name)  # Output: Fido
print(my_dog.species)  # Output: dog
my_dog.make_sound()  # Output: Bark

print(my_cat.name)  # Output: Whiskers
print(my_cat.species)  # Output: cat
my_cat.make_sound()  # Output: Meow
