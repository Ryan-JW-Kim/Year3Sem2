from db_manager import Database
from display import Display

class User:    
    def __init__(self):
        self.db_interface = Database
        self.available_commands = []
        self.cmd = None
        self.type = "Super User"

        self.run_loop = True
        self.has_no_command = True
    
    def is_valid_cmd(self, cmd: str):
        if cmd in self.available_commands:
            return True

    def prompt_command(self):
    
        cmds = f"Choose from the following commands:"
        for cmd in self.available_commands:
            cmds += f"\n   - {cmd}"
        cmds += "\n\nEnter a command: "
        temp = input(cmds)
        self.run_loop = True if temp not in Display.exit_commands else False

        while self.run_loop:

            if not self.is_valid_cmd(temp):
                print("Invalid command. Please try again.")
                temp = input(cmds)
                self.run_loop = True if temp not in Display.exit_commands else False

            else:
                self.cmd = temp
                self.has_no_command = False
                break

        print("\n")
        
        return temp

    def do(self, cmd: str):
        print("Error...this method must be overwritten.")