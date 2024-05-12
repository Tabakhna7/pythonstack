class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        self.balance=balance
        self.int_rate=int_rate
    
    def deposit(self, amount):
        self.balance+=amount
        return self    
    def withdraw(self, amount):
        if self.balance>amount:
            self.balance-=amount
        if self.balance<amount:
            print (" not enough amount")
        return self
    def display_account_info(self):
        print(f"your balance is {self.balance} and interest rate {self.int_rate}")
        return self
    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        return self


user1= BankAccount( .01,300 ).deposit(400).deposit(300).deposit(20).withdraw(100).withdraw(50).yield_interest().display_account_info()

user2=BankAccount( .03,300 ).deposit(500).deposit(100).withdraw(200).yield_interest().display_account_info()

user3=BankAccount(.06).deposit(800).withdraw(1000).display_account_info()


