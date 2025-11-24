import os

class ShoppingCart:
    def __init__(self):
        self.listt = []
        while True:
            os.system("cls")
            if self.listt == []:
                print("Shopping Cart is Empty")
            else:
                for i in self.listt:
                    print(i)
            item = input("Enter item to the Cart: ")
            if item != "\n":
                self.listt.append(item)
            else:
                break

s1 = ShoppingCart()