from abc import ABC,abstractmethod
from datetime import date

class Account(ABC):
    count=0
    def __init__(self,balance):
        Account.count+=1
        self.__account_no=f"ACC-{Account.count:03}"
        self.__balance=balance
        self.__created_at=date.today()
        
    @property
    def account_no(self):
        return self.__account_no
    @property
    def created_at(self):
        return self.__created_at
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        if amount<self.get_minimum_allowed_floor():
            raise ValueError("Transaction rejected: Balance cannot drop below zero!")
        self.__balance=amount
    
    def get_minimum_allowed_floor(self):
        return 0
    
    @abstractmethod
    def account_type(self):
        pass
    @abstractmethod
    def interest_rate(self):
        pass
    
    def deposit(self,amount):
        if amount<0:
            raise ValueError("Transaction rejected: Balance cannot drop below zero!")
        self.balance+= amount
        print(f"Deposited: Rs.{amount}. New Balance: Rs.{self.balance}")
        
        
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Withdrawal amount must be positive!")
        self.balance -= amount  
        print(f"Withdrew: Rs.{amount}. New Balance: Rs.{self.balance}")
        
    def __str__(self):
        return f"{self.account_no} | {self.account_type()} | Rs.{self.balance} | {self.created_at}"
    
    
    
class SavingsAccount(Account):
    def __init__(self, balance,rate=0.05):
        super().__init__(balance)
        self.__interest_rate=rate
    
    def account_type(self):
        return type(self).__name__
    
    def interest_rate(self):
        return self.__interest_rate
    
    def add_interest(self):
        self.balance*= (1 + self.interest_rate())
        print(f"Interest Applied! New Balance: Rs.{self.balance:.2f}")
    
    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Withdrawal amount must be positive!")
        if self.balance-amount<1000:
            raise ValueError("minimum Rs.1000 must remain")
        super().withdraw(amount)
    
    

    
class CurrentAccount(Account):
    def __init__(self, balance,overdraft_limit = 10000):
        self.__overdraft_limit=overdraft_limit
        super().__init__(balance)
        
    
    def account_type(self):
        return type(self).__name__
    
    def interest_rate(self):
        return 0
    
    def get_minimum_allowed_floor(self):
        return -self.__overdraft_limit
    
    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Withdrawal amount must be positive!")
        if self.balance-amount<self.get_minimum_allowed_floor():
            raise ValueError("can go negative up to overdraft limit")
        super().withdraw(amount)
    
    
    
    
    