from book import Book
from database import Database

# TODO: make sure only one book with the same title and author can be in the library

class Library:
    def __init__(self, database: Database):
        self.books = []
        self.database = database

    def add_book(self, book):
        self.database.insert_book(book)
        self.load_books()

    def view_books(self):
        if not self.books:
            print("This library has no books.")
        else:
            for b in self.books:
                print(b.title)

    def search_books(self, search_parameter):
        matching_titles: list[Book] = []

        for b in self.books:
            if search_parameter.lower() in b.title.lower():
                matching_titles.append(b)

        if not matching_titles:
            print("No books found matching that title.")
            return
        else:
            for b in matching_titles:
                print(b.title)

    def load_books(self):
        self.books = self.database.get_all_books()

    def update_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower(): 
                print("Book: " + book.title)
                print("Current Status: " + book.status)
                print("Current Rating: " + str(book.rating) + "\n")

                id: int | None = book.id

                if id is None:
                    raise ValueError("ID cannot be None when updating book.") 
 
                status = Book.validate_status(input("New Status: "))
                rating = Book.validate_rating(input("New Rating: "))

                self.database.update_book(id, status, rating)
                self.load_books()
                return

        print("There are no books in the library with that title.")

    def delete_book(self, title: str, author: str):
        deleted_book: list[tuple] = self.database.delete_book(title.title(), author.title())

        if len(deleted_book) == 1:
            print(f"\"{deleted_book[0][0]}\" by {deleted_book[0][1]} has been removed from the library.")
            self.load_books()
            return
        
        print("There are no books in the library with that title and by that author.")
        


