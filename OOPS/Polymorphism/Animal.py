class Animal:
    def sound(self):
        return "Raises a Sound"
class Dog(Animal):
    def sound(self):
        return "Dog Barks"
class Cat(Animal):
    def sound(self):
        return "Cat Meows"
obj=Dog()
print(obj.sound())
obj=Animal()
print(obj.sound())
obj=Cat()
print(obj.sound())