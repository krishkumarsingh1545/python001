#Create an Employee class with salary raise function
#Create Book class that stores title, author, and price; display details
#Create a MovieTicket class with discount based on age
#Build a Rectangle class to calculate area and perimeter
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary
    
    def details(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.dept}")
        print(f"Salary: {self.salary}")
    
    def salaryRaise(self):
        self.salary+=(0.10*self.salary)

e1 = Employee("Krish", "Developer", 20000)
e1.details()
e1.salaryRaise()
e1.details()