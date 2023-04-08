from user import User

class Staff(User):
    def __init__(self, db_interface):
        super(Staff, self).__init__(db_interface)
        
        self.available_commands = ["Get Book", "Reserve Book", "Add Book", "Delete Book", "Checkout Book", "Help"]
        self.type = "staff"
        self.db_interface = db_interface

    def do(self):
        
        if self.cmd == "Add Book":
            self.db_interface.add_book(self)

        elif self.cmd == "Checkout Book":
            self.db_interface.checkout_book(self)

        elif self.cmd == "Reserve Book":
            self.db_interface.reserve_book(self)

        elif self.cmd == "Help":
            self.db_interface.display.help()

        elif self.cmd == "Get Book":
            self.db_interface.get_book(self)

        self.has_no_command = True