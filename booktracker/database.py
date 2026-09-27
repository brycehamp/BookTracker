import sqlite3
from book import Book

class Database:
    def __init__(self, database_path: str):
        self.database_path = database_path

    def initialize_database(self):
        connection = sqlite3.connect(self.database_path)

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            status TEXT NOT NULL,
            rating REAL NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            """
            )

        connection.commit()
        connection.close()

    def insert_book(self,book: Book):
        connection = sqlite3.connect(self.database_path)
        
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO books (title, author, genre, status, rating)
            VALUES (?,?,?,?,?,?)
            """,
            (book.title, book.author, book.genre, book.status, book.rating, book.id)
            )

        connection.commit()
        connection.close()

    def delete_book(self, title: str, author: str) -> list[tuple]:
        connection = sqlite3.connect(self.database_path)

        cursor = connection.cursor()

        deleted_row = cursor.execute("""
        DELETE FROM books
        WHERE title = ?
        AND author = ?
        RETURNING title, author
        """,
        (title, author)
        ).fetchall()

        connection.commit()
        connection.close()

        return deleted_row

    def get_all_books(self) -> list[Book]:
        connection = sqlite3.connect(self.database_path)
            
        cursor = connection.cursor()

        cursor.execute("""
            Select *
            From books
            """
            )

        books_rows = cursor.fetchall()

        connection.close()

        books: list[Book] = []

        for row in books_rows:
            books.append(Book(row[1], row[2], row[3], row[4], row[5], row[0]))

        return books