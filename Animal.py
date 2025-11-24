class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.sound()
    def sound(self):
        print("Barks, barks")

class Cat(Animal):
    def sound(self):
        print("Meow, meow")
    def __init__(self):
        super().__init__()
        self.sound()

d1 = Dog()
c1 = Cat()