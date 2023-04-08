from user import User

class Student(User):
    def __init__(self, db_interface):
        super(Student, self).__init__(db_interface)
        
        self.available_commands = ["Get Book", "Reserve Book", "Help"]
        self.type = "student"
        self.db_interface = db_interface

    def do(self):

        if self.cmd == "Reserve Book":
            self.db_interface.reserve_book(self)

        elif self.cmd == "Help":
            self.db_interface.display.help()

        elif self.cmd == "Get Book":
            self.db_interface.get_book(self)
        
        self.has_no_command = True