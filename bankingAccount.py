# educative task 1 of inheritance
# int object is not callable error occur because we use int as function
class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    def withdrawal(self,amount):

        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount

    def getbalance(self):
        return self.balance

class SavingAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate=interestRate

    def interestAmount(self):
        return ((self.interestRate*self.balance)/100)
sa=SavingAccount("mark",2000,5)
print("Mark balance :",sa.getbalance())
sa.deposit(600)
print("Balance after deposit",sa.getbalance())
print("interest rate is :",sa.interestAmount())