class User:
     def  __init__(self,username=None,balance=None):
          self.username = username
          self.account = BankAccount()
     def withdrwal(self,amount):
          if self.account.balance<amount:
               print("your balance is lees than the needed withdrawl")
               return
          self.account.withdraw(amount)
          
     def deposite(self,DepositeAmount):
               self.account.deposit(DepositeAmount)
               
     def displayUserBalance(self):
          self.account.display_account_info()

     def transferMoney(self,trgetperson=None,transferamount=None):
          
          if transferamount > self.balance:
               print("no balance to transfer")
               return
          else:
               trgetperson.deposite(transferamount)
               self.withdrwal(transferamount)
               
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
            return self
		
    def display_account_info(self):
        print(f"your balance is {self.balance} ")
        return self
    
ibraheem=User()
ibraheem.deposite(123)
ibraheem.withdrwal(100)
ibraheem.displayUserBalance()