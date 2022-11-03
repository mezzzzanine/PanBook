import sqlite3


class Search:
    def search(self, b_name):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql.execute(f"SELECT id FROM server WHERE name = '{b_name}'")
        return (sql.fetchone()[1])

        db.commit()
        db.close()

