from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        return 2*math.pi*self.radius
    def area(self):
        return  math.pi*(self.radius**2)
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def area(self):
        return self.length*self.breadth
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def perimeter(self):
        return self.side1+self.side2+self.side3
    def area(self):
        s=(self.side1+self.side2+self.side3)/2
        return math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
obj1=Rectangle(10,20)
obj2=Rectangle(20,30)
obj3=Circle(40)
obj4=Triangle(50,60,70)
print(obj1.perimeter())
print(obj2.perimeter())
print(obj3.perimeter())
print(obj4.perimeter())
print(obj4.area())