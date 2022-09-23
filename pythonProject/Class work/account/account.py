class Account:
    balance = 0

    def __init__(self, name):
        self.name = name

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance += amount

    def transfer(self, amount, name):
        self.withdraw(amount)
        name.deposit(amount)
        return name.balance
