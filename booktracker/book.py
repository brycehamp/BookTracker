class Book:
    def __init__(self, title: str, author: str, genre: str, status: str, rating: float):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        self.rating = rating

    def to_dict(self):
        book = {"title": self.title, 
                "author": self.author, 
                "genre": self.genre,
                "status": self.status,
                "rating": self.rating}
        
        return book

    @staticmethod
    def create_book():
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

        return book
