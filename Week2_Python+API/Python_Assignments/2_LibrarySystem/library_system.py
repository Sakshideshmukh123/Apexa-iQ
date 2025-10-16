import sys
import os
from datetime import datetime, timedelta

# Redirect output to output.txt in the same folder
output_file = os.path.join(os.path.dirname(__file__), 'output.txt')
sys.stdout = open(output_file, 'w')

# ----------------- Classes -----------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.borrowed_by = None
        self.due_date = None
    
    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by} (Due: {self.due_date})"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}), Books borrowed: {len(self.books_borrowed)}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}
    
    def add_book(self, book):
        self.books[book.book_id] = book
        return f"Book '{book.title}' added to the library."
    
    def add_member(self, member):
        self.members[member.member_id] = member
        return f"Member {member.name} registered."
    
    def borrow_book(self, book_id, member_id):
        if book_id not in self.books:
            return "Book not found in library."
        if member_id not in self.members:
            return "Member not registered in library."
        
        book = self.books[book_id]
        member = self.members[member_id]
        
        if not book.is_available:
            return f"Book '{book.title}' is already borrowed."
        
        book.is_available = False
        book.borrowed_by = member.name
        book.due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        member.books_borrowed.append(book_id)
        
        return f"Book '{book.title}' borrowed by {member.name}. Due date: {book.due_date}"
    
    def return_book(self, book_id):
        if book_id not in self.books:
            return "Book not found in library."
        
        book = self.books[book_id]
        
        if book.is_available:
            return f"Book '{book.title}' was not borrowed."
        
        member_name = book.borrowed_by
        for member in self.members.values():
            if member.name == member_name and book_id in member.books_borrowed:
                member.books_borrowed.remove(book_id)
        
        book.is_available = True
        book.borrowed_by = None
        book.due_date = None
        
        return f"Book '{book.title}' returned successfully."
    
    def display_available_books(self):
        available_books = [book for book in self.books.values() if book.is_available]
        if not available_books:
            return "No books available."
        
        result = "Available Books:\n"
        for book in available_books:
            result += f"{book}\n"
        return result
    
    def display_borrowed_books(self):
        borrowed_books = [book for book in self.books.values() if not book.is_available]
        if not borrowed_books:
            return "No books currently borrowed."
        
        result = "Borrowed Books:\n"
        for book in borrowed_books:
            result += f"{book}\n"
        return result

# ----------------- Example usage -----------------
if __name__ == "__main__":
    # Create library
    city_library = Library("City Public Library")
    
    # Add books
    book1 = Book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("B002", "To Kill a Mockingbird", "Harper Lee")
    book3 = Book("B003", "1984", "George Orwell")
    
    print(city_library.add_book(book1))
    print(city_library.add_book(book2))
    print(city_library.add_book(book3))
    
    # Add members
    member1 = Member("M001", "Alice Johnson")
    member2 = Member("M002", "Bob Smith")
    
    print(city_library.add_member(member1))
    print(city_library.add_member(member2))
    
    # Borrow books
    print(city_library.borrow_book("B001", "M001"))
    print(city_library.borrow_book("B002", "M002"))
    
    # Display books
    print(city_library.display_available_books())
    print(city_library.display_borrowed_books())
    
    # Return a book
    print(city_library.return_book("B001"))
    
    # Display updated books
    print(city_library.display_available_books())

# Close the redirected stdout
sys.stdout.close()
