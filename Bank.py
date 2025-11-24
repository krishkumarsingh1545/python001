#Create BAnkAccount Class with deposit and withdraw method

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    balance = 0
    def currentBal(self):
        print(f"Current Balance: {self.balance}")
    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        self.balance-=amount

b1 = BankAccount()
b1.balance = 100
b1.deposit(100)
b1.currentBal()
b1.withdraw(20)
b1.currentBal()