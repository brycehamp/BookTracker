# region Imports
from book import Book
from library import Library
# endregion

# region Variables 
library = Library()
# endregion 

# region Execute
while True:
    choice = input("What would you like to do? \n 1. Add book \n 2. View books \n 3. Search for a book \n 4. Exit \n Choice: ")
    
    while True:
        try:
            choice = int(choice)
            break
        except ValueError:
            choice = input("Selection is not an integer. Please try again. Selection: ")

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
            library.save_books()

        case 2:
            library.view_books()

        case 3:
            library.search_books(input("Enter search parameters: "))

        case 4:
            break

        case _:
            print("Invalid menu selection. Please try again.")

# endregion




