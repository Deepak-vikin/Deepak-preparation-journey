class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.borrowed_books=[]

class Student(User):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept = dept
    def get_Student_name(self):
        return self.name
    def borrow_limit(self):
        return 3
    def get_Student_age(self):
        return self.age
    def get_Student_department(self):
        return self.dept
class Teacher(User):
    def __init__(self,name,age):
        super().__init__(name,age)
    def borrow_limit(self):
        return 5
    def get_Teacher_name(self):
        return self.name
    def get_Teacher_age(self):
        return self.age
class Book:
    def __init__(self,name,price,status):
        self.name = name
        self.price = price
        self.status = "Available"
    def get_Book_name(self):
        return self.name
    def get_Book_price(self):
        return self.price
    def borrow(self):
        self.status = "Available"
    def return_book(self):
        self.status = "Not Available"
    def get_Book_status(self):
        return self.status
class Library():
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def borrow_book(self,user,book):
        if book not in self.books:
            print("Book Not Available in Library")
            return
        if book.get_Book_status() == "Not Available":
            print("Book Already Borrowed")
            return
        if len(user.borrowed_books)>=user.borrow_limit():
            print("Limit Reached You Cant Borrow Further")
            return
        user.borrowed_books.append(book)
        book.borrow()
        print(user.name,"Borrowed Book",book.get_Book_name())
    def return_books(self,user,book):
        if book not in user.borrowed_books:
            print("You Didnt Borrow This Book")
            return
        user.borrowed_books.remove(book)
        book.return_book()
        print(user.name,"Returned Book",book.get_Book_name())




