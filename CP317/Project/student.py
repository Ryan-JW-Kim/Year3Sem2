from user import User

class Student(User):
    def __init__(self, db_interface):
        super(Student, self).__init__(db_interface)
        
        self.available_commands = ["search", "reserve", "help"]
        self.type = "student"
        self.db_interface = db_interface

    def do(self):
        
        if self.cmd == "search":
            self.db_interface.search(self)
        elif self.cmd == "reserve":
            self.db_interface.reserve(self)
        elif self.cmd == "help":
            self.db_inerface.display.help()

        self.has_no_command = True