import sqlite3
import file_explorer

class DBController():
    PASSWORD = 'escentric'

    def add_book(self, b_name, b_author, b_r_year, genre):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql.execute(f"INSERT INTO books VALUES ('{b_name}','{b_author}','{0}','{int(b_r_year)}, {genre}')")
        db.commit()
        db.close()

    def remove_book(self, id):
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql.execute(f"DELETE FROM books WHERE id = '{int(id)}'")
        db.commit()
        db.close()

    def sentry(self, user_password):
        if  self.PASSWORD == self.user_password:
            pass
        else:
            pass 

    def choose_option(self, option_type):
        if option_type == "add":
            pass
        elif option_type == "remove":
            pass
        else:
            pass
