from book import Book
from library import Library

book1 = Book("The Atlas Six", "Olivie Blake", "Dark Academia", "Read", 4.5)
book2 = Book("Starside", "Alex Aster", "Romantasy", "Read", 3.5)
book3 = Book("He Who Fights with Monsters 11", "Travis Deverell", "LitRPG", "Want to Read", 5)

books: list[Book] = [book1, book2, book3]

library = Library()

for b in books:
    library.add_book(b)

for b in library.books:
    print(b.title)