from database_control import Dbcontrol


class Charts:
    def __init__(self):
        self.library = Dbcontrol()

    def charts(self):
        return self.library.get_charts()
