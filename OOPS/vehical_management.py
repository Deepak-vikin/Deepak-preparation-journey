class Vehical:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed
    def display_details(self):
        return {f"Vehical Brand : {self.brand} "
        f"Vehical Model : {self.model} "
        f"Vehical Speed : {self.speed}"}
    def start(self):
        return "Vehical Started"
class Car(Vehical):
    def __init__(self,brand,model,speed,fuel_type,number_of_doors):
        super().__init__(brand,model,speed)
        self.fuel_type=fuel_type
        self.number_of_doors=number_of_doors
class Bike(Vehical):
    def __init__(self,brand,model,speed,engine_cc,has_gear):
        super().__init__(brand,model,speed)
        self.engine_cc=engine_cc
        self.has_gear=has_gear
class SportsCar(Car):
    def __init__(self,brand,model,speed,fuel_type,number_of_doors,has_turbo,fully_tuned):
        self.has_turbo=has_turbo
        self.fully_tuned=fully_tuned
    def display_details(self):
        return {"Brand":self.brand,
                "Model":self.model,
                "speed":self.speed,
                "fuel_type":self.fuel_type,
                "No_of_doors":self.number_of_doors,
                "Has Turbo ?":self.has_turbo,
                "Fully Tuned ?":self.fully_tuned}
car = SportsCar(
    "Porsche", "911 GT3",300,
    "Petrol", 2,
    True,False
)
print(car.display_details())