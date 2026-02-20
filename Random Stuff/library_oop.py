'''
# Project Creation Date: 5:35:15 PM, 2/19/2026
'''

import time as t

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.good_condition = True

    def __repr__(self):
        if self.good_condition:
            if self.available:
                av = "Available"
            else:
                av = "Borrowed"
        else:
            av = "Terminated"
        return f"{self.title} : {self.author} : {self.isbn} : {av}"

    def mark_available(self):
        if self.good_condition:
            if self.available:
                return f"{self.title} is already available."
            else:
                self.available = True
                return f"{self.title} is now available."
        else:
            return terminated(self.title)
        
    def mark_borrowed(self):
        if self.good_condition:
            if not self.available:
                return f"{self.title} is already borrowed."
            else:
                self.available = False
                return f"{self.title} is now borrowed."
        else:
            return terminated(self.title)
    
    def check_availability(self):
        if self.good_condition:
            if self.available:
                return f"{self.title} is available."
            else:
                return f"{self.title} is currently borrowed."
        else:
            return terminated(self.title)
    
    def terminate(self):
        self.good_condition = False
        return f"{self.title} has been thrown away."

def terminated(title):
    return f"{title} is in the trash due to old age."

def add_book():
    title = input("What is the title of the book?\n>")
    author = input("Who is the author of the book?\n>")
    isbn = input("What is the ISBN number for the book?\n>")

    books.append(Book(title, author, isbn))

books = []
help_command = """At any time, you can type: 
      'add' to add a book
      'borrow' to mark a book as borrowed
      'return' to mark a book as available
      'search' to search for a book by ISBN number
      'display' to show all books in the library
      'terminate' to terminate an old book\n"""

print("Hello, welcome to your digital library!\nLet's add your first book.")
add_book()
print(f"\nAwesome! You have now added your first book to the library.\nHere is the list as of now: \n")
print(f"{books}\n")
t.sleep(4)
print(help_command)
t.sleep(7)
print("That is the complete tutorial, you are free to use the platform.")
t.sleep(2)

while True:
    commands = ["add", "borrow", "display", "help", "return", "search", "terminate"]
    command = input("\nType a command (type 'help' to view all commands):\n>").lower()
    if command not in commands:
        print("Not a valid command.")
        continue

    if command == "add":
        add_book()
    elif command == "borrow":
        num = input("What is the book's ISBN number?")
        for book in books:
            if book.isbn == num:
                print("Book found!")
                print(book.mark_borrowed())
                break
        else: 
            print("Book not found in library")
    elif command == "display":
        for book in books:
            print(book)
    elif command == "help":
        print(help_command)
    elif command == "return":
        num = input("What is the book's ISBN number?")
        for book in books:
            if book.isbn == num:
                print("Book found!")
                print(book.mark_available())
                break
        else: 
            print("Book not found in library")
    elif command == "search":
        num = input("What is the book's ISBN number?")
        for book in books:
            if book.isbn == num:
                print("Book found!")
                print(book)
                break
        else: 
            print("Book not found in library")
    elif command == "terminate":
        num = input("What is the book's ISBN number?")
        for book in books:
            if book.isbn == num:
                print("Book found!")
                print(book.terminate())
                break
        else: 
            print("Book not found in library")