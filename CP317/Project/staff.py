from user import User

class Staff(User):
    def __init__(self, db_interface):
        super(Staff, self).__init__(db_interface)
        
        self.available_commands = ["add", "delete", "update", "search", "checkout", "help", "get books"]
        self.type = "staff"
        self.db_interface = db_interface

    def do(self):
        
        if self.cmd == "add":
            self.db_interface.add_book(self)
        elif self.cmd == "delete":
            self.db_interface.delete(self)
        elif self.cmd == "update":
            self.db_interface.update(self)
        elif self.cmd == "search":
            self.db_interface.search(self)
        elif self.cmd == "checkout":
            self.db_interface.checkout(self)
        elif self.cmd == "help":
            self.db_interface.display.help()
        elif self.cmd == "get books":
            self.db_interface.get_books(self)

        self.has_no_command = True