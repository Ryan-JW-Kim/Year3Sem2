from user import User

class Staff(User):
    def __init__(self, db_interface):
        super(Staff, self).__init__(db_interface)
        
        self.available_commands = []
        self.type = "staff"
        self.db_interface = db_interface

    def do(self):
        
        self.has_no_command = True