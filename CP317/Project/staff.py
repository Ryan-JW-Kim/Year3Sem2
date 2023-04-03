from display import *
from user import User

class Staff(User):
    def __init__(self):
        super(Staff, self).__init__()
        
        self.available_commands = ["Add", "Delete", "Update", "Search", "Checkout", "Help"]
        self.type = "Staff"


    def do(self, cmd:str):
        
        if cmd == "Add":
            self.db_interface.add_book(self)
        elif cmd == "Delete":
            self.db_interface.delete(self)
        elif cmd == "Update":
            self.db_interface.update(self)
        elif cmd == "Search":
            self.db_interface.search(self)
        elif cmd == "Checkout":
            self.db_interface.checkout(self)
        elif cmd == "Help":
            Display.help()