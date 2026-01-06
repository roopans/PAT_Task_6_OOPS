from selenium.webdriver.support.expected_conditions import none_of

# Base class for bank accounts
class customers:
    def __init__(self,account_number,balance):
        self.Account_number=account_number
        self.Account_balance=balance

    def print_balance(self):
        print(self.Account_number,self.Account_balance)

    def deposit(self, amount):
        self.Account_balance += amount
        print(f"Deposited {amount}. New balance is {self.Account_balance}.")

    def withdraw(self, amount):
        self.Account_balance -= amount
        if amount > self.Account_balance:
            print("Insufficient funds.")
        else:
            print(f"Withdrew {amount}. New balance is {self.Account_balance}.")


#  Child class for Savings Account
class Savingsaccount(customers):
    def __init__ (self,account_number,balance,interest_rate):
        super().__init__(account_number,balance)
        self.interest_rate=interest_rate

class currentaccount(customers):
    def __init__ (self,account_number,balance,Minimum_balance):
        super().__init__(account_number,balance)
        self.Minimumbalance=Minimum_balance

show_customers = Savingsaccount("123456",1000,3.5)
# show_customers.print_balance()

currentaccount_customers = currentaccount("654321",2000,500)
# currentaccount_customers.print_balance()
# Get deposit and withdraw details for savings account
show_customers.deposit(200)
show_customers.withdraw(5000)
# Get deposit current account details
currentaccount_customers.withdraw(5000)
currentaccount_customers.deposit(400)



