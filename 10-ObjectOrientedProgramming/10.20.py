class Account():
    def __init__(self):
        self.balance = 0
        self.number = "11111111111111111111111111"

    def deposit(self, amount):
        print("Checking if you can deposit...")
        self.amount= amount
        self.balance += amount

    def withdraw(self, amount):
        print("Checking if you can withdraw...")
        self.amount = amount
        if amount > self.balance:
            print("You can't do that!")
        else:
            self.balance -= amount

    def change_number(self, changed_number):
        self.number=changed_number

    def display(self):
        print(f"Your account ({self.number}) has {self.balance} on it.")

acc = Account()
acc.display()
acc.change_number("12 3456 5555 9090 1111 0000 7722")
acc.display()
acc.deposit(25.3)
acc.display()
acc.withdraw(31.7)
acc.display()
acc.withdraw(14)
acc.display()