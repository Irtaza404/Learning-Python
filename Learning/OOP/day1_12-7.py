class BankAccount:
    bank="HBL"
    total_accounts=0
    
    def __init__(self,owner,balance):
        if balance<0:
            raise ValueError("balance can't be negative")
        self.owner=owner
        self.balance=balance
        # self.bank="UBL"
        BankAccount.total_accounts+=1
        self.account_no=BankAccount.bank+"-"+str(BankAccount.total_accounts)        
    def __repr__(self):
        return f"BankAccount('Ali', 5000)"
    
    # Python __str__
    def __str__(self):
        return f"{self.owner} Rs.{self.balance}"

    def deposit(self,amount):
        if amount<0:
            raise ValueError("amount can't be negative")
        self.balance+=amount
    
    def withdraw(self,amount):
        if amount<0:
            raise ValueError("amount can't be negative")
        if amount>self.balance:
            raise ValueError(" insufficient amount")
        self.balance-=amount
        
    def details(self):
        print(f"name: {self.owner} , balance={self.balance} ,Account no ={self.account_no}")












b1=BankAccount("Claude",0)
b2=BankAccount("Irtaza",0)
b1.details()
b2.details()
print(BankAccount.total_accounts)
print(b1)   # should show nice output
repr(b1)    # should show developer output

class Car:
    pass

class phone:
    pass

class  BankAccount:
    pass














