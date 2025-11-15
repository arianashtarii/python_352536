# Superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I'm Animal!"

    def move(self):
        return "Moving..."


# Subclass
class Cat(Animal):
    def speak(self):
        return "Meow Meow..."

    def climb(self):
        return "Climbing..."


# Subclass دیگر
class Bird(Animal):
    def speak(self):
        return "jik jik..."

    def move(self):  # بازنویسی متد والد
        return "Flying..."



cat = Cat("Cat")
bird = Bird("Bird")

print(cat.speak())
print(bird.speak())
print(bird.move())