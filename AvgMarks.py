#Create a Student class with attributes and methods to calculate average marks

class Student:
    def __init__(self, name, p, c, m):
        self.name = name
        self.p = p
        self.c = c
        self.m = m
    
    def average(self):
        print(f"Name {self.name} \nAverage: {((self.p+self.c+self.m)/3)}")

s1 = Student("Krish", 78, 89, 87)
s1.average()