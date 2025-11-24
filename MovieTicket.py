#Create a MovieTicket class with discount based on age

class MovieTicket:
    def __init__(self, movie, price, age):
        self.discount = 0
        self.price = price
        self.movie = movie
        if age<18:
            self.price-=(self.price*0.10)
            self.discount = 10
        elif age>18 and age<36:
            self.discount = 30
            self.price-=(self.price*0.30)
        else:
            self.price = price
        self.details()
    
    def details(self):
        print(f"Movie: {self.movie}")
        print(f"Price: ${self.price}")
        print(f"Discount Given: {self.discount}%")

m1 = MovieTicket("Spiderman", 40, 12)
