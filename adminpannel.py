from database_control import Dbcontrol


class DBController:
    PASSWORD = 'escentric'

    def __init__(self):
        """Create object"""
        self.library = Dbcontrol()

    def add_book(self, b_name, b_author, b_r_year, genre):
        self.library.add(b_name, b_author, b_r_year, genre)
