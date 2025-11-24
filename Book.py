#Create Book class that stores title, author, and price; display details
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = float(price)
        self.details()
    
    def details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

b1 = Book("Death Note", "Tsugumi Obha", 200)
