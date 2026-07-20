from abc import ABC, abstractmethod
from datetime import date,datetime
import re

class Account(ABC):
    count = 0

    def __init__(self, balance):
        Account.count += 1
        self.__account_no = f"ACC-{Account.count:03}"
        self.__balance = balance
        self.__created_at = date.today()
        self.__transaction=[]

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
    def balance(self, amount):
        if amount < self.get_minimum_allowed_floor():
            raise ValueError("Transaction rejected: Balance cannot drop below zero!")
        self.__balance = amount

    def get_minimum_allowed_floor(self):
        return 0

    @abstractmethod
    def account_type(self):
        pass

    @abstractmethod
    def interest_rate(self):
        pass

    def deposit(self, amount,txn_type="DEPOSIT"):
        if amount < 0:
            raise ValueError("Transaction rejected: Balance cannot drop below zero!")
        self.balance += amount
        self.__transaction.append(Transaction(txn_type=txn_type,amount=amount,account_no=self.account_no,balance_after=self.balance))
        print(f"Deposited: Rs.{amount}. New Balance: Rs.{self.balance}")

    def withdraw(self, amount,txn_type="WITHDRAW"):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        self.balance -= amount
        self.__transaction.append(Transaction(txn_type=txn_type,amount=amount,account_no=self.account_no,balance_after=self.balance))
        print(f"Withdrew: Rs.{amount}. New Balance: Rs.{self.balance}")

    def transaction_history(self):
        return self.__transaction.copy()
    
    def mini_statement(self,n=5):
        for statement in self.transaction_history()[-n:][::-1]:
            print(statement)
            
    def __str__(self):
        return f"{self.account_no} | {self.account_type()} | Rs.{self.balance:,.0f} | {self.created_at}"

    def transfer(self, other_account, amount):
        if amount <= 0:
            raise ValueError("transfer amount must be positive!")
        self.withdraw(amount, "TRANSFER_OUT")
        try:
            other_account.deposit(amount, "TRANSFER_IN")
        except Exception:
            self.deposit(amount, "WITHDRAW")  # rollback
            raise
        print("Transaction done")
        
    def generate_receipt(self, txn_id):
        for transaction in self.transaction_history():
            if transaction.txn_id == txn_id:
                return transaction.receipt()
        raise ValueError("Transaction id not found in transaction history")

class SavingsAccount(Account):
    def __init__(self, balance, rate=0.05):
        super().__init__(balance)
        self.__interest_rate = rate

    def account_type(self):
        return type(self).__name__

    def interest_rate(self):
        return self.__interest_rate

    def add_interest(self):
        self.balance *= 1 + self.interest_rate()
        print(f"Interest Applied! New Balance: Rs.{self.balance:.2f}")

    def withdraw(self, amount, txn_type="WITHDRAW"):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if self.balance - amount < 1000:
            raise ValueError("minimum Rs.1000 must remain")
        super().withdraw(amount, txn_type)

class CurrentAccount(Account):
    def __init__(self, balance, overdraft_limit=10000):
        self.__overdraft_limit = overdraft_limit
        super().__init__(balance)

    def account_type(self):
        return type(self).__name__

    def interest_rate(self):
        return 0

    def get_minimum_allowed_floor(self):
        return -self.__overdraft_limit

    def withdraw(self, amount, txn_type="WITHDRAW"):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if self.balance - amount < self.get_minimum_allowed_floor():
            raise ValueError("can go negative up to overdraft limit")
        super().withdraw(amount, txn_type)


class Customer:
    count = 0

    def __init__(self, name, phone):
        Customer.count += 1
        self.__id = f"CUS-{Customer.count:03}"
        self.name = name
        self.phone = phone
        self.__accounts = []
        self.__created_at = date.today()

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if not name.replace(" ","").isalpha() or len(name)<3:
            raise ValueError("must be string, min 3 chars")
        self.__name=name
            

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self,phone):
        if not re.search(r"^03\d{2}-\d{7}$",phone):
            raise ValueError("invalid phone number")
        self.__phone=phone
    
    @property
    def accounts(self):
        return self.__accounts.copy()
    
    @property
    def created_at(self):
        return self.__created_at
    
    def open_account(self,account):
        if len(self.accounts)==3:
            raise ValueError("max 3 accounts per customer")
        if account in self.accounts:
            raise ValueError("can't add same account twice")
        self.__accounts.append(account)
            
    def close_account(self,account_no):
        if (target := self.get_account(account_no)) is not None:
            if len(self.accounts)!=1:
                self.__accounts.remove(target)
                print(f"Successfully removed {target}")
            else:
                raise ValueError("can't close last account")
        
    def get_account(self,account_no):
        if len(self.accounts)==0:
            raise ValueError("No accounts opened yet under this customer profile.")
        for account in self.accounts:
            if account.account_no==account_no:
                return account
        return None

    def total_balance(self):
        return sum(acc.balance for acc in self.accounts)
    
    def __str__(self):
        return f"{self.id} | {self.name} | {self.phone} | {len(self.accounts)} accounts | Rs.{self.total_balance()}"
    
    
    
class Transaction:
    count=0
    def __init__(self,txn_type,amount,account_no,balance_after):
        Transaction.count+=1
        self.__txn_id=f"TXN-{Transaction.count:03}" 
        self.__txn_type=txn_type
        self.__amount=amount
        self.__timestamp=datetime.now()
        self.__account_no=account_no
        self.__balance_after=balance_after
    
    def __str__(self):
        return f"{self.txn_id} | {self.txn_type} | Rs.{self.amount} | {self.account_no} | {self.timestamp}"
    
    @property
    def txn_id(self):
        return self.__txn_id
    
    @property
    def txn_type(self):
        return self.__txn_type
    
    @property
    def account_no(self):
        return self.__account_no
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def timestamp(self):
        return self.__timestamp
    
    @property
    def balance_after(self):
        return self.__balance_after
    
    def receipt(self):
        return (
            f"----- TRANSACTION RECEIPT -----\n"
            f"Txn ID     : {self.txn_id}\n"
            f"Type       : {self.txn_type}\n"
            f"Amount     : Rs.{self.amount:,.0f}\n"
            f"Account    : {self.account_no}\n"
            f"Balance    : Rs.{self.balance_after:,.0f}\n"
            f"Date       : {self.timestamp.strftime('%d-%m-%Y %H:%M')}\n"
            f"--------------------------------"
    )
    