import json
from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        if not self.books:
            print("This library has no books.")
        else:
            for b in self.books:
                print(b.title)

    def search_books(self, search_parameter):
        matching_titles = []

        for b in self.books:
            if search_parameter.lower() in b.title.lower():
                matching_titles.append(b)

        if not matching_titles:
            return ("No books found matching that title.")
        else:
            for b in matching_titles:
                print(b.title)

    def save_books(self):
        list_of_books = []

        for b in self.books:
            list_of_books.append(b.to_dict())

        with open("booktracker/books.json", "w") as file:
            json.dump(list_of_books, file, indent=4)

    def load_books(self):
        try:
            with open("booktracker/books.json", "r") as file:
                library_books_data = json.load(file)

                for book_data in library_books_data:
                    book = Book(book_data["title"], 
                                book_data["author"], 
                                book_data["genre"], 
                                book_data["status"], 
                                book_data["rating"])
                    self.add_book(book)
        except FileNotFoundError:
            self.save_books()

    def update_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower(): 
                print("Book: " + book.title)
                print("Current Status: " + book.status)
                print("Current Rating: " + str(book.rating) + "\n")
 
                status = Book.validate_status(input("New Status: "))

                rating = Book.validate_rating(input("New Rating: "))

                book.status = status
                book.rating = rating
                return

        print("There are no books in the library with that title.")

    def delete_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"\"{book.title}\" has been removed from the library.")
                return

        print("There are no books in the library with that title.")


