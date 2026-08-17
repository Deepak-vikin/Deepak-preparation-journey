from abc import ABC,abstractmethod
class Bird(ABC):
    @abstractmethod
    def fly(self):
        print("fly")
    @abstractmethod
    def eat(self):
        print("eat")
class landbird(ABC):
    @abstractmethod
    def eat(self):
        print("eat")
class penguin(landbird):
    def eat(self):
        print("penguin")
class sparrow(Bird):
    def eat(self):
        print("sparrow")
    def fly(self):
        print("fly")
bird1=sparrow()
bird1.eat()
bird1.fly()
bird2=penguin()
bird2.eat()
from Encapsulation import Class_Bank as B
obj=B.Bank(111,"Ajay",5000)
print(obj._Bank__Balance)