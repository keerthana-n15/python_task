class Author:

    def __init__(self, author_id, author_name):
        self.author_id = author_id
        self.author_name = author_name

class Student:

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class Book:

    def __init__(self, book_id, book_name, author, student):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.student = student

    def display(self):
        print("Book ID      :", self.book_id)
        print("Book Name    :", self.book_name)
        print("Author ID    :", self.author.author_id)
        print("Author Name  :", self.author.author_name)
        print("Student ID   :", self.student.student_id)
        print("Student Name :", self.student.student_name)


author1 = Author(101, "James")
author2 = Author(102, "John")
author3 = Author(103, "David")


student1 = Student(201, "Riya")
student2 = Student(202, "Rahul")
student3 = Student(203, "Anita")

book1 = Book(1, "Python Programming", author1, student1)
book2 = Book(2, "Java Basics", author2, student2)
book3 = Book(3, "Database Systems", author3, student3)


books = [book1, book2, book3]
for book in books:
    book.display()