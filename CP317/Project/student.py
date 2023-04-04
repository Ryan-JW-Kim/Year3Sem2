from user import User

class Student(User):
    def __init__(self, db_interface):
        super(Student, self).__init__(db_interface)
        
        self.available_commands = []
        self.type = "student"
        self.db_interface = db_interface

    def do(self):
        
        self.has_no_command = True