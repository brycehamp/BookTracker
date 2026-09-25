import sqlite3

def initialize_database():
    connection = sqlite3.connect("booktracker/books.db")

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

def insert_book(book):
    connection = sqlite3.connect("booktracker/books.db")
    
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO books (title, author, genre, status, rating)
        VALUES (?,?,?,?,?)
        """,
        (book.title, book.author, book.genre, book.status, book.rating)
        )

    connection.commit()
    connection.close()

def get_all_books():
    connection = sqlite3.connect("booktracker/books.db")
        
    cursor = connection.cursor()

    cursor.execute("""
        Select *
        From books
        """
        )

    rows = cursor.fetchall()

    connection.commit()
    connection.close()
    return rows