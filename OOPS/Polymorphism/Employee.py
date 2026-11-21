class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    def calculate_salary(self):
        return 20000
class Developer(Employee):
    def __init__(self,name,emp_id,bonus):
        super().__init__(name,emp_id)
        self.bonus=bonus
    def calculate_salary(self):
        return 40000+self.bonus
class Manager(Employee):
    def __init__(self,name,emp_id,allowance):
            super().__init__(name,emp_id)
            self.allowance=allowance
    def calculate_salary(self):
        return 60000+self.allowance
employees = [
    Developer("Deepak", 101, 5000),
    Manager("Arun", 102, 10000),
    Employee("Karthik", 103)
]
for employee in employees:
    print(employee.name, employee.calculate_salary())

