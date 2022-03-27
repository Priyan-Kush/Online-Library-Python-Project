class Library:
    def __init__(self, listofbooks):
        self.books= listofbooks
    
    def displayAvailableBooks(self):
        print("Books present in this library are:\n")
        for books in self.books:
            print(books)
            

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued the book {bookname}.")
            self.books.remove(bookname)
            return True
        else:
            print("The book is not available or has already been issued  by someone else/\n")
            return False
    
    def returnBook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returnig this book.")

class Student:
        def requestBook(self):
            self.book= input("Enter the name of the book:\n")
            return self.book
        def returnBook(self):
            self.book= input("Enter the name of the bookyou want to return:\n")
            return self.book

if __name__ == "__main__":
    centraLibrary = Library(["DSA", "Django", "C for Noobs", "Python Notes", "Web Dev", "FLutter Dev"])
    student = Student()
    # centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n WELCOME TO CENTRAL LIBRARY
                           THE BEST ONLINE LIBRARY SYSTEM
                            Please choose an option:
                            1. List all the books
                            2. Request a book
                            3. Add/Return a book
                            4. Exit the Librarys
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Online Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
        