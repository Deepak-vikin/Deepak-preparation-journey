class Student():
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def totalmarks(self):
        return sum(self.get_marks())
    def averagemarks(self):
        return sum(self.get_marks())/len(self.get_marks())
    def grade(self):
        grades=[]
        for mark in self.get_marks():
            if mark>90:
                grades.append("A")
            elif mark>80:
                grades.append("B")
            elif mark>70:
                grades.append("C")
            elif mark>60:
                grades.append("D")
            elif mark>50:
                grades.append("E")
            else:
                grades.append("F")
        return grades
obj=Student("Ajay",99,[100,90,80,40,20])
print(obj.grade())
print(obj.totalmarks())
print(obj.averagemarks())