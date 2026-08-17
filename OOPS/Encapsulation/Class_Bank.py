class Bank():
    def __init__(self,accNo,Name,Balance):
        self.accNo = accNo
        self.Name = Name
        self.__Balance = Balance
    def get_balance(self):
        return self.__Balance
    def set_balance(self,Balance):
        self.__Balance = Balance
    def deposit(self,amount):
        if amount > 0:
            amt=amount+self.get_balance()
            self.set_balance(amt)
            print("Amount deposited")
    def withdraw(self,amount):
        if self.get_balance() >= amount:
            amt=self.get_balance()-amount
            self.set_balance(amt)
            print("Amount withdrawn")
        else:
            print("Not enough money")
accNo=input("Enter Account Number: ")
Name=input("Enter Name: ")
Balance=int(input("Enter Balance: "))
B=Bank(accNo,Name,Balance)
while True:
    print("1. Deposit \n 2. Withdraw \n 3. Check Current Balance \n 4. Exit")
    choice=int(input("Enter Choice: "))
    match choice:
        case 1:
            print("Enter Amount To be Deposited:")
            amount=int(input())
            B.deposit(amount)
        case 2:
            print("Enter Amount To be Withdrawn:")
            amount=int(input())
            B.withdraw(amount)
        case 3:
            bal=B.get_balance()
            print("Current Balance is: ",bal)
        case 4:
            exit("Thank You")



