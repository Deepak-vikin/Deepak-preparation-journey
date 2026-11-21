class A:
    def show(self):
        return "A"
class B:
    def show(self):
        return "B"
class C(B,A):
    pass
obj=C()
print(obj.show())
print(C.mro())