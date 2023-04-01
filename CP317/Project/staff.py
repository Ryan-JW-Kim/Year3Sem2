from Utils import text
class Staff:
    
    @staticmethod
    def perform_command(cmd):
        if cmd == "add":
            Staff.add_command()
        elif cmd == "delete":
            Staff.delete_staff()
        elif cmd == "edit":
            Staff.edit_staff()
        elif cmd == "search":
            Staff.search()
        
    @staticmethod
    def add_command():

        print("What would you like to add? (book, student, staff)")

        cmd = text["Input Prompt"]

        if cmd == "book":
            book_data = {}
            pass

        elif cmd == "student":
            student_data = {}
            pass

        elif cmd == "staff":
            staff_data = {}
            pass
