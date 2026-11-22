class Product:
    def __str__(self):
        return f"Product Name :{self.name} ,Product Price:{self.price}"
    def __init__(self,name,price,quantity):
        self.name=name
        if price>=0:
            self.price=price
        else:
            raise ValueError("PRICE CANT BE IN NEGATIVE")
        if quantity>0:
            self.quantity=quantity
        else:
            raise ValueError("QUANTITY CANT BE NONE OR IN NEGATIVE")
    def __add__(self,other):
        return self.price*self.quantity + other.price*other.quantity
class ShoppingCart:
    def __init__(self):
        self.cart=[]
    def add_product(self,*products):
        for i in products:
            self.cart.append(i)
    def calculate_total(self):
        total=0
        for i in self.cart:
            total+=i.price*i.quantity
        return total
    def __len__(self):
        return len(self.cart)
product1=Product("Ice cream",50,-1)
product2=Product("Biscuit",90,5)
Cart1=ShoppingCart()
Cart1.add_product(product1,product2)
print(Cart1.calculate_total())
print(len(Cart1))
print(product1+product2) 

