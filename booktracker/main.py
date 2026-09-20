# region Imports
from book import Book
from library import Library
# endregion

# region Variables 
library = Library()
# endregion 

# region Execute

# library books need to be loaded from json file before any input.
# having this at the beginning also prevents issues with saving new books to the json file later.
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
            library.save_books()

        case 2:
            library.view_books()

        case 3:
            library.search_books(input("Enter search parameters: "))

        case 4:
            library.update_book(input("Enter the title of the book you would like to update: "))
            library.save_books()

        case 5:
            library.delete_book(input("Enter the title of the book you would like to delete: "))
            library.save_books()

        case 6:
            break

        case _:
            print("Invalid menu selection. Please try again.")

# endregion