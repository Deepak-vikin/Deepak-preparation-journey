class Vehical:
    def __init__(self,brand,speed,fuel):
            self.brand = brand
            self.speed = speed
            self.fuel = fuel
    def retrieve_info(self):
        return f"Brand: {self.brand},Speed: {self.speed},Fuel Type: {self.fuel}"
class Car(Vehical):
    def __init__(self,brand,speed,fuel,NOofDorrs):
        super().__init__(brand,speed,fuel)
        self.Noofdoors=NOofDorrs
    def display(self):
        info = super().retrieve_info()
        print(info)
        print("Number of Doors:",self.Noofdoors)
class Bike(Vehical):
    def __init__(self,brand,speed,fuel,hasGear):
        super().__init__(brand,speed,fuel)
        self.hasGear=hasGear
    def display(self):
        info=super().retrieve_info()
        print(info)
        print("Has Gears ? :",self.hasGear)
class Truck(Vehical):
    def __init__(self,brand,speed,fuel,loadcap):
        super().__init__(brand,speed,fuel)
        self.loadcap=loadcap
    def display(self):
        info=super().retrieve_info()
        print(info)
        print("Load Capacity :",self.loadcap)
obj1=Car("Mercedes",80,"Petrol",5)
obj1.display()
obj2=Bike("Kawasaki",80,"Petrol","Yes")
obj2.display()
obj3=Truck("Scania",80,"Petrol",50)
obj3.display()
