class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
class Developer(Employee):
    def __init__(self,name,age,salary,coding_bonus):
        super().__init__(name,age,salary)
        self.coding_bonus = coding_bonus
    def calculateSalary(self):
        return self.salary+self.coding_bonus
class Designer(Employee):
    def __init__(self,name,age,salary,design_bonus):
        super().__init__(name,age,salary)
        self.design_bonus = design_bonus
    def calculateSalary(self):
        return self.salary+self.design_bonus
class Manager(Employee):
    def __init__(self,name,age,salary,management_bonus):
        super().__init__(name,age,salary)
        self.management_bonus= management_bonus
    def calculateSalary(self):
        return self.salary+self.management_bonus
emp=[Developer("Sachin",20,10000,1000),Designer("Ajay",19,4000,500),Manager("Vikram",30,7000,1000)]
for employee in emp:
    print(employee.name)
    print(employee.age)
    print(employee.calculateSalary())