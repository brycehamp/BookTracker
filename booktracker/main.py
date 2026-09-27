# region Imports
from book import Book
from library import Library
from database import Database
# endregion

# region Variables 
database = Database("booktracker/books.db")
library = Library(database)
# endregion 

# region Execute

# database must be initialized and books must be loaded before any input.
database.initialize_database()
library.load_books()

while True:
    choice = input("What would you like to do? \n 1. Add book \n 2. View books \n 3. Search for a book \n 4. Update a book \n 5. Remove a book \n 6. Exit \n Choice: ")
    
    while True:
        try:
            choice = int(choice)
            break
        except ValueError:
            choice = input("Selection is not an integer. Please try again. Selection: ")

    match choice:
        case 1:
            book = Book.create_book()
            library.add_book(book)

        case 2:
            library.view_books()

        case 3:
            library.search_books(input("Enter search parameters: "))

        case 4:
            library.update_book(input("Enter the title of the book you would like to update: "))

        case 5:
            library.delete_book(input("Enter the title of the book you would like to delete: "), 
                                input("Enter the author of the book you would like to delete: "))

        case 6:
            break

        case _:
            print("Invalid menu selection. Please try again.")

# endregion