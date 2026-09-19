import json
from book import Book 

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
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
        list_of_books = [] # a list of all the books with all their attributes

        for b in self.books:
            list_of_books.append(b.to_dict())

        with open("booktracker/books.json", "w") as file:
            json.dump(list_of_books, file, indent=4)