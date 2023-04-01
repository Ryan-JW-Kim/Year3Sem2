
class Display:
    
    @staticmethod
    def perform_command(cmd):
        if cmd == "display":
            Display.display()
        

class Help
    @staticmethod
    def print_help():
        msg = """
        Welcome to the Library Management System...
        Below are the commands you can use and the order in which they can be used:
        1. \"add\" - add a new book, student or staff member
        2. \"delete\" - delete a book, student or staff member
        3. \"edit\" - edit a book, student or staff member
        4. \"search\" - search for a book, student or staff member
        5. \"reserve\" - reserve a book
        """
        print(msg)
    
    @staticmethod
    def print_invalid_command():
        print("Invalid command")