# encapsulation 

class Phone:
    def __init__(self):
        self.__name="Oppo"


p=Phone()
print(p._Phone__name)# WTF

class BankAccount:
    bank="HBL"
    total_accounts=0
    
    def __init__(self,owner,balance):
        if balance<0:
            raise ValueError("balance can't be negative")
        self.owner=owner
        self.__balance=balance
        # self.bank="UBL"
        BankAccount.total_accounts+=1
        self.account_no=BankAccount.bank+"-"+str(BankAccount.total_accounts)        
    def __repr__(self):
        return f"BankAccount('Ali', 5000)"
    
    # Python __str__
    def __str__(self):
        return f"{self.owner} Rs.{self.__balance}"

    def deposit(self,amount):
        if amount<0:
            raise ValueError("amount can't be negative")
        self.__balance+=amount
    
    def withdraw(self,amount):
        if amount<0:
            raise ValueError("amount can't be negative")
        if amount>self.__balance:
            raise ValueError(" insufficient amount")
        self.__balance-=amount
        
    def details(self):
        print(f"name: {self.owner} , balance={self.__balance} ,Account no ={self.account_no}")
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def bal(self,a):
        self.__balance=a


b=BankAccount("ali",10000)
b.bal=100
print(b.balance)





