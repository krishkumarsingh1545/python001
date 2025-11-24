class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        super().__init__()
        print(f"Area of rectangle: {self.area(l, b)}")
        
    def area(self, l, b):
        return l*b

class Square(Shape):
    def __init__(self, s):
        super().__init__()
        print(f"Area of square: {self.area(s)}")
        
    def area(self, s):
        return pow(s, 2)
    
s1 = Square(3)
r1 = Rectangle(3, 23)