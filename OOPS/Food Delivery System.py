from abc import ABC,abstractmethod
class user:
    def __init__(self,name,phone,email):
        self.__name=name
        self.__phone=phone
        self.__email=email
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email

class Customer(user):
    def __init__(self,name,phone,email,Cust_id):
        super().__init__(name,phone,email)
        self.__Cust_id=Cust_id
    def get_Cust_id(self):
        return self.__Cust_id

class Manager(user):
    def __init__(self,name,phone,email,manager_id):
        super().__init__(name,phone,email)
        self.__manager_id=manager_id
    def get_manager_id(self):
        return self.__manager_id

class Order:
    def __init__(self,fooditems,prices,Orderid):
        self.fooditems=fooditems
        self.prices=prices
        self.Orderid=Orderid
    def get_fooditems(self):
        return self.fooditems
    def get_prices(self):
        for food,price in zip(self.fooditems,self.prices):
            print(food,price)
    def total_cost(self):
        return sum(self.prices)
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("UPI amount paid :",amount)
class CreditCard(Payment):
    def pay(self,amount):
        print("Credit card amount paid :",amount)
class Cash(Payment):
    def pay(self,amount):
        print("Cash amount paid :",amount)
customers=[["Ajay",912831249,"deasfskjgn",234324],["Vijay",238237498,"sfgjdsgff",43243]]
for cust in customers:
    obj=Customer(cust[0],cust[1],cust[2],cust[3])
    order=Order(["Pizza","Burger"],[100,150],23234)
    order.get_fooditems()
    total=order.total_cost()
    payment=UPI()
    payment.pay(total)


