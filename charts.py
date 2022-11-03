import sqlite3

class Charts:
    def get_charts(self):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql.execute("""
SELECT * FROM books
SORT BY downloads """)
