# Superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Sound!!!"


# Subclass
class Dog(Animal):
    def speak(self):
        return "Woof Woof!!!"

    def run(self):
        return "Running..."


my_dog = Dog("Dog")
print(my_dog.speak())
print(my_dog.name)