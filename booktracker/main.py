# region Imports
from book import Book
from library import Library
# endregion

# region Variables 
library = Library()
choice = 0
# endregion 

# region Execute
while choice != 3:
    match choice:
        case 1:
            title: str = input("Title: ")
            author: str = input("Author: ")
            genre: str = input("Genre: ")
            status: str = input("Status: ")
            rating = input("Rating: ")

            while True:
                try:
                    rating = float(rating)
                    break
                except ValueError:
                    rating = input("Rating is not a number. Please try again. Rating: ")

            book = Book(title, author, genre, status, rating)
            library.add_book(book)

        case 2:
            for b in library.books:
                print(b.title)

    choice = input("What would you like to do? \n 1. Add book \n 2. View books \n 3. Exit \n Choice: ")

    while True:
        try:
            choice = int(choice)
            break
        except ValueError:
            choice = input("Selection is not an integer. Please try again. Selection: ")

# endregion




