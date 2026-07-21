from abc import ABC, abstractmethod
from datetime import date, datetime
import re
import time

class Account(ABC):
    count = 0

    def __init__(self, balance):
        Account.count += 1
        self.__account_no = f"ACC-{Account.count:03}"
        self.__balance = balance
        self.__created_at = date.today()
        self.__transaction = []
        self.__frozen = False

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

    @property
    def is_frozen(self):
        return self.__frozen

    @is_frozen.setter
    def is_frozen(self, value):
        self.__frozen = value

    def get_minimum_allowed_floor(self):
        return 0

    @abstractmethod
    def account_type(self):
        pass

    @abstractmethod
    def interest_rate(self):
        pass

    def deposit(self, amount, txn_type="DEPOSIT"):
        if self.is_frozen:
            raise PermissionError("Account is frozen")
        if amount < 0:
            raise ValueError("Transaction rejected: Balance cannot drop below zero!")
        self.balance += amount
        self.__transaction.append(
            Transaction(
                txn_type=txn_type,
                amount=amount,
                account_no=self.account_no,
                balance_after=self.balance,
            )
        )
        print(f"Deposited: Rs.{amount}. New Balance: Rs.{self.balance}")

    def withdraw(self, amount, txn_type="WITHDRAW"):
        if self.is_frozen:
            raise PermissionError("Account is frozen")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        self.balance -= amount
        self.__transaction.append(
            Transaction(
                txn_type=txn_type,
                amount=amount,
                account_no=self.account_no,
                balance_after=self.balance,
            )
        )
        print(f"Withdrew: Rs.{amount}. New Balance: Rs.{self.balance}")

    def transaction_history(self):
        return self.__transaction.copy()

    def mini_statement(self, n=5):
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
    def name(self, name):
        if not name.replace(" ", "").isalpha() or len(name) < 3:
            raise ValueError("must be string, min 3 chars")
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not re.search(r"^03\d{2}-\d{7}$", phone):
            raise ValueError("invalid phone number")
        self.__phone = phone

    @property
    def accounts(self):
        return self.__accounts.copy()

    @property
    def created_at(self):
        return self.__created_at

    def open_account(self, account):
        if len(self.accounts) == 3:
            raise ValueError("max 3 accounts per customer")
        if account in self.accounts:
            raise ValueError("can't add same account twice")
        self.__accounts.append(account)

    def close_account(self, account_no):
        if (target := self.get_account(account_no)) is not None:
            if len(self.accounts) != 1:
                self.__accounts.remove(target)
                print(f"Successfully removed {target}")
            else:
                raise ValueError("can't close last account")

    def get_account(self, account_no):
        if len(self.accounts) == 0:
            raise ValueError("No accounts opened yet under this customer profile.")
        for account in self.accounts:
            if account.account_no == account_no:
                return account
        return None

    def total_balance(self):
        return sum(acc.balance for acc in self.accounts)

    # in Customer class
    def _force_close(self, account_no):
        target = self.get_account(account_no)
        if target:
            self.__accounts.remove(target)

    def __str__(self):
        return f"{self.id} | {self.name} | {self.phone} | {len(self.accounts)} accounts | Rs.{self.total_balance()}"


class Transaction:
    count = 0

    def __init__(self, txn_type, amount, account_no, balance_after):
        Transaction.count += 1
        self.__txn_id = f"TXN-{Transaction.count:03}"
        self.__txn_type = txn_type
        self.__amount = amount
        self.__timestamp = datetime.now()
        self.__account_no = account_no
        self.__balance_after = balance_after

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


class Admin:
    count = 0

    def __init__(self, name, password):
        Admin.count += 1
        self.__id = f"ADM-{Admin.count:03}"
        self.__name = name
        self.__password = password

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def authenticate(self, password):
        return password == self.__password

    def change_password(self, old, new):
        if self.authenticate(old):
            self.__password = new
        else:
            raise ValueError("Incorrect old password")

    def add_customer(self, bank, name, phone):
        # check if name already exists
        for c in bank.customers:
            if c.name.lower() == name.lower() and c.phone == phone :
                raise ValueError(f"Customer '{name}'  with {phone} already exists")
        customer = Customer(name, phone)
        bank.register_customer(customer)
        return customer
    def get_customer(self, bank, customer_id):
        return bank.find_customer(customer_id)

    def list_customer(self, bank):
        for customer in bank.customers:
            print(customer)

    def freeze_account(self, account):
        account.is_frozen = True

    def unfreeze_account(self, account):
        account.is_frozen = False

    def force_close_account(self, bank, customer_id, account_no):
        customer = bank.find_customer(customer_id)
        customer._force_close(account_no)

    # bank_summary(bank) → prints full bank report
    def bank_summary(self, bank):
        frozen = list(bank.frozen_accounts())

        print("════════════════════════════════════")
        print(f"{''+bank.name+' BANK REPORT':^36}")
        print("════════════════════════════════════")
        print(f"Total Customers  : {len(bank.customers)}")
        print(f"Total Accounts   : {sum(len(c.accounts) for c in bank.customers)}")
        print(f"Total Deposits   : Rs.{bank.total_deposits():,}")
        print(f"Frozen Accounts  : {len(frozen)}")
        print("════════════════════════════════════")
        print("CUSTOMERS:")
        for c in bank.customers:
            plural = "s" if len(c.accounts) != 1 else ""
            print(
                f"  {c.id} | {c.name:<6} | {len(c.accounts)} account{plural} | Rs.{c.total_balance():,}"
            )
        print("════════════════════════════════════")

    def apply_interest_all(self, bank):
        for account in list(bank.accounts_by_type("SavingsAccount")):
            account.add_interest()

    def monthly_statement(self, account):
        today = date.today()
        # filter transactions from current month
        monthly = [
            txn
            for txn in account.transaction_history()
            if txn.timestamp.month == today.month and txn.timestamp.year == today.year
        ]

        total_in = sum(
            t.amount for t in monthly if t.txn_type in ("DEPOSIT", "TRANSFER_IN")
        )
        total_out = sum(
            t.amount for t in monthly if t.txn_type in ("WITHDRAW", "TRANSFER_OUT")
        )

        print("════════════════════════════════════")
        print(f"{'MONTHLY STATEMENT':^36}")
        print(f"Account  : {account.account_no}")
        print(f"Month    : {today.strftime('%B %Y')}")
        print("════════════════════════════════════")

        if not monthly:
            print("  No transactions this month")
        else:
            for txn in monthly:
                print(
                    f"  {txn.txn_id} | {txn.txn_type:<12} | Rs.{txn.amount:>10,.0f} | {txn.timestamp.strftime('%d-%m-%Y %H:%M')}"
                )

        print("════════════════════════════════════")
        print(f"  Total In    : Rs.{total_in:,.0f}")
        print(f"  Total Out   : Rs.{total_out:,.0f}")
        print(f"  Closing Bal : Rs.{account.balance:,.0f}")
        print("════════════════════════════════════")


class Bank:
    def __init__(self, name):
        self.__name = name
        self.__customers = []
        self.__admin = Admin("Irtaza", "12345")
    @property
    def admin(self):
        return self.__admin
    @property
    def name(self):
        return self.__name

    @property
    def customers(self):
        return self.__customers.copy()

    def register_customer(self, customer):
        self.__customers.append(customer)

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer_id == customer.id:
                return customer
        return None

    def accounts_by_type(self, account_type):
        for account in list(self.all_accounts()):
            if account.account_type() == account_type:
                yield account

    def all_accounts(self):
        for customer in self.__customers:
            for account in customer.accounts:
                yield account

    def frozen_accounts(self):
        for account in list(self.all_accounts()):
            if account.is_frozen:
                yield account

    def top_customers(self, n=3):
        return sorted(self.customers, key=lambda x: x.total_balance(), reverse=True)[:n]

    def total_deposits(self):
        return sum(acc.balance for acc in self.all_accounts())

    def __str__(self):
        return f"{self.__name} Bank | {len(self.customers)} customers | Rs.{self.total_deposits():,} total deposits"


class CLI:
    
    
    def get_int(self, prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number")
            return None
    def get_account(self, customer):
        acc_no = input("Account number: ")
        account = customer.get_account(acc_no)
        if account is None:
            print("Account not found")
        return account
    def get_customer(self,bank):
        id=input("Customer ID :")
        customer=bank.find_customer(id)
        if customer is None:
            print("customer not found")
        return customer
        
    def main(self):
        bank=Bank("HBL")
        while True:
            try:
                print("════════════════════════")
                print("     HBL BANK SYSTEM")
                print("════════════════════════")
                print("1. Admin Login")
                print("2. Customer Login")
                print("3. Exit")
                print("════════════════════════")
                match self.get_int("Choice:=>"):
                    case 1:
                        for _ in range(3):
                            name=input("name :")
                            password=input("Password :")
                            if bank.admin.name==name and bank.admin.authenticate(password):
                                self.admin_menu(bank)
                                break
                            else:
                                print("Invalid name and password")
                        else:
                            print("time out, wait 30 sec to login again")
                            time.sleep(30)
                    case 2:
                        for _ in range(3):
                            if (customer:=self.get_customer(bank)) is not None:
                                self.customer_menu(customer,bank)
                                break
                        else:
                            print("time out, wait 30 sec to login again")
                            time.sleep(30)
                    case 3:
                        print("exiting...")
                        return
                    case _:print("Invalid input")
            except ValueError:
                print("incorrect input type")

    def admin_menu(self,bank):
        while True:
            try:
                admin=bank.admin
                print("════════════════════════")
                print("     Admin menu")
                print("════════════════════════")
                print("1. Add Customer")
                print("2. List Customers")
                print("3. Freeze Account")
                print("4. Unfreeze Account")
                print("5. Bank Summary")
                print("6. Apply Interest (All Savings)")
                print("7. Monthly Statement")
                print("8. Top Customers")
                print("9. Logout")
                print("════════════════════════")
                match self.get_int("Choice:=>"):
                    case 1:
                        name=input("name:")
                        phone=input("phone:")
                        try:
                            admin.add_customer(bank, name, phone)
                            print("Customer added!")
                        except ValueError as e:
                            print(e)
                    case 2:admin.list_customer(bank)
                    case 3:
                        if (customer:=self.get_customer(bank)) is not None:
                            if (account:=self.get_account(customer)) is not None:
                                admin.freeze_account(account)
                    case 4:
                        if (customer:=self.get_customer(bank)) is not None:
                            if (account:=self.get_account(customer)) is not None:
                                admin.unfreeze_account(account)
                    case 5:
                        admin.bank_summary(bank)
                    case 6:
                        admin.apply_interest_all(bank)
                    case 7:
                        if (customer:=self.get_customer(bank)) is not None:
                            if (account:=self.get_account(customer)) is not None:
                                admin.monthly_statement(account)                        
                    case 8:
                        for customer in bank.top_customers():
                            print(customer)
                    case 9:
                        print("logout...")
                        return
                    case _:print("Invalid input")
            except ValueError:
                print("incorrect input type")

    def customer_menu(self,customer,bank):
        while True:
            try:
                print("════════════════════════")
                print("     customer menu")
                print("════════════════════════")
                print("1. View Accounts")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Mini Statement")
                print("6. Transaction History")
                print("7. Logout")
                print("════════════════════════")
                match self.get_int("Choice:=>"):
                    case 1:
                        for account in customer.accounts:
                            print(account)
                    case 2:
                        account=self.get_account(customer)
                        if account is not None:
                            account.deposit(float(input("Enter amount :")))
                    case 3:
                        account=self.get_account(customer)
                        if account is not None:
                            account.withdraw(float(input("Enter amount :")))
                    case 4:
                        account=self.get_account(customer)
                        other_customer = self.get_customer(bank)
                        other = self.get_account(other_customer)
                        if account is not None and other is not None:
                            account.transfer(other,float(input("Enter amount :")))
                    case 5:
                        account=self.get_account(customer)
                        if account is not None:
                            account.mini_statement()
                    case 6:
                        account=self.get_account(customer)
                        if account is not None:
                            for t in account.transaction_history():
                                print(t)
                    case 7:
                        print("logout...")
                        return
                    case _:print("Invalid input")
            except ValueError:
                print("incorrect input type")

if __name__ == "__main__":
    cli = CLI()
    cli.main()
    



