class user:
     
     def  __init__(self,username=None,balance=None):
          self.username = username
          self.balance = balance
     
     def withdrwal(self,amount):
          if self.balance<amount:
               print("your balance is lees than the needed withdrawl")
               return
          self.balance =self.balance-amount
          
     def deposite(self,DepositeAmount):
               self.balance=self.balance+DepositeAmount
               
     def displayUserBalance(self):
          print(f"mrs/mrs {self.username}")
          print(f"your balance is {self.balance} $" )
          return self.balance

     def transferMoney(self,trgetperson=None,transferamount=None):
          
          if transferamount > self.balance:
               print("no balance to transfer")
               return
          else:
               trgetperson.deposite(transferamount)
               self.withdrwal(transferamount)
          
          
     
user1=user("tabkhna", 150)
user2=user("saed", 70)
user3=user("shatha",35000)
# user1.deposite(151)
# user1.deposite(305)
# user1.deposite(153)
# user1.withdrwal(300)
# user1.displayUserBalance()
# user2.deposite(300)
# user2.deposite(140)
# user2.withdrwal(100)
# user2.withdrwal(220)
# user2.displayUserBalance()
# user3.deposite(5000)
# user3.withdrwal(1000)
# user3.withdrwal(8700)
# user3.withdrwal(12000)
# user3.displayUserBalance()
user1.transferMoney(user2,30)
user1.displayUserBalance()
user2.displayUserBalance()