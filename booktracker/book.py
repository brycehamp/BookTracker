class Book:
    def __init__(self, title: str, author: str, genre: str, status: str, rating: float, id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        self.rating = rating
        self.id = id

    def to_dict(self) -> dict:
        book = {"title": self.title, 
                "author": self.author, 
                "genre": self.genre,
                "status": self.status,
                "rating": self.rating}
        
        return book

    @staticmethod
    def create_book() -> Book:
        title: str = input("Title: ")
        author: str = input("Author: ")
        genre: str = input("Genre: ")
        status: str = Book.validate_status(input("Status: "))
        rating = Book.validate_rating(input("Rating: "))

        book = Book(title.title(), author.title(), genre.capitalize(), status.capitalize(), rating)

        return book

    @staticmethod
    def validate_rating(rating) -> float:
        while True:
            try:
                rating = float(rating)
                if not 0.0 <= rating <= 5.0:
                    rating = input("Rating is not between 0 and 5. Please Try again. Rating: ")
                else:
                    break
            except ValueError:
                rating = input("Rating is not a number. Please try again. Rating: ")

        return rating

    @staticmethod
    def validate_status(status: str) -> str:
        status_options = ["want to read", "read", "reading"]

        while True:
            if status.lower() in status_options:
                break
            else:
                status = input("You have entered an invalid status. Please choose \"Want to Read\", \"Read\", or \"Reading.\" Status: ")

        status = status.capitalize()
        return status
        
