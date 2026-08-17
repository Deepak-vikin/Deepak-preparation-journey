from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self,amount):
        print(f"Payed {amount} using UPI")

class CreditCard(Payment):
    def pay(self,amount):
        print(f"Payed {amount} using Credit Card")

class Cash(Payment):
    def pay(self,amount):
        print(f"Payed {amount} using Cash")

obj1=Cash()
obj1.pay(100)
obj2=CreditCard()
obj2.pay(100)
obj3=UPI()
obj3.pay(100)