from database_control import Dbcontrol

class Search:
    def __init__(self):
        self.library = Dbcontrol()

    def find_book(self, book_name):
        self.library.read(book_name)

