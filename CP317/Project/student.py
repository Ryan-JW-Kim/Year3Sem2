from display import *
from db_manager import *

class Student(User):
    def __init__(self):
        super(Student, self).__init__()
        
        self.available_commands = ["Search", "Reseerve", "Help"]
        self.type = "Student"

    def do(self, cmd:str):
        
        if cmd == "Search":
            self.db_interface.search(self)
        elif cmd == "Reserve":
            self.db_interface.reserve(self)
        elif cmd == "Help":
            Display.help()
