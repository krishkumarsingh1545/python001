#Build a Rectangle class to calculate area and perimeter
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
        print(f"Area of rectangle: {l*b}")

r1 = Rectangle(8, 4)