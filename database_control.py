import sqlite3


class Dbcontrol:
    def __init__(self):
        """Connect to database"""
        self.conn = sqlite3.connect('server.db')
        self.cursor = self.conn.cursor()

    def add(self, book_name, book_autors, realise_year, genre):
        """Add book to database"""
        self.cursor.execute(f"""INSERT INTO books (book_name, book_autors, realise_year, genre) 
                                VALUES '{book_name}', '{book_autors}', '{realise_year}', '{genre}' ;""")
        self.conn.close()
        self.conn.commit()

    def read(self, book_name):
        """Get book from database"""
        self.cursor.execute(f"""SELECT id
                                FROM books
                                WHERE book_name LIKE '%{book_name}%'; """)
        result = self.cursor.fetchone()[1]
        self.conn.close()
        self.conn.commit()
        return result
    
    def get_charts(self):
        """Get book from database"""
        self.cursor.execute(f"""SELECT book_name
                                FROM books
                                ORDER BY downloads
                                LIMIT 10;""")
        result = self.cursor.fetchall()
        self.conn.close()
        self.conn.commit()
        return result
