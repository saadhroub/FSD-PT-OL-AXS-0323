class Address:
    def __init__(self, city,street, phone ,email):
        self.city = city
        self.street = street
        self.phone= phone
        self.email = email



class BankAccount:
    def __init__(self, int_rate=0.2, balance=0):
        self.balance = balance
        self.rate = int_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bank_account = BankAccount(int_rate=0, balance=0)
        self.address = Address(city="",street="", phone="" ,email="")

    def deposit(self, amount):
        self.bank_account.deposit(amount)

    def withdraw(self, amount):
        self.bank_account.withdraw(amount)

    def get_balance(self):
        return self.bank_account.get_balance()

