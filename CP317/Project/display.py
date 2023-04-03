from student import Student
from staff import Staff

class Display:

    valid_user_types = ["student", "staff"]
    exit_commands = ["quit", "exit"]

    @staticmethod
    def prompt_user_type(db_interface):

        prompt = "Are you a \"student\" or \"staff\" member? "

        user_type = input(prompt)

        while user_type not in Display.exit_commands:

            if user_type not in Display.valid_user_types:
                print("Invalid user type. Please try again.")
                user_type = input(prompt)

            else:
                break

        if user_type == "student":
            return Student(db_interface)
        
        elif user_type == "staff":
            return Staff(db_interface)
        
    @staticmethod
    def prompt_for_query(find: str, valid: type, query: str = ""):

        prompt = f"Enter {find}: "

        temp = input(prompt)

        while temp not in Display.exit_commands:

            if type(temp) is not valid:
                print("Invalid input. Please try again.")
                temp = input(prompt)

            else:
                break

        query += f"WHERE {find} = {temp}"

        return query
    
    @staticmethod
    def help():
        print("Help")
        return True