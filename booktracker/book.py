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
