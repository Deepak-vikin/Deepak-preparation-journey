class BankAccount:
    def __init__(self,account_holder,acc_no,balance):
        self.account_holder=account_holder
        self.acc_no=acc_no
        self.__balance=balance
    def display_acc_details(self):
        details={"Holder Name":self.account_holder,
                 "Account Number":self.acc_no, 
                 "Current Balance":self.__balance}
        return details
    def deposit(self,deposit_amt):
        if deposit_amt > 0:
            self.__balance+=deposit_amt
            return f"Amount {deposit_amt} deposited"
        else:
            return "Money cant be in Negative"
    def withdraw(self,amount):
        if amount<=0:
            return "Money cant be negative"
        if self.__balance-amount < 0 :
            return "Not enough money ! "
        self.__balance-=amount
        return f"Amount {amount} Withdrawn"
    def get_balance(self):
        return self.__balance
account = BankAccount("Deepak", "12345", 5000)
# print(account.__balance) returns Error
print(account._BankAccount__balance)
print(account.get_balance())  # 5000

account.deposit(2000)
account.withdraw(1000)

print(account.get_balance())  # 6000