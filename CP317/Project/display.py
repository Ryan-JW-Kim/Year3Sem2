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
    def prompt_for_query(params: dict, origin, query):

        # list of valid user inputs
        valid = [param["Display Name"] for param in params]

        # What to input will be used for
        action = params[0]["Action"]
        prompt = f"Select one of the following fields to use when performing \"{action}\":\n"
        
        # For each possible field, display it to the user
        for param in params:
            name = param["Display Name"]
            prompt += f"   - {name}\n"

        # Prompt the user for type input
        while origin.run_loop:
            temp = input(prompt)
            origin.run_loop = True if temp not in origin.db_interface.display.exit_commands else False

            if temp not in valid:
                print("Invalid input. Please try again.")
                prompt = f"Select one of the following fields {valid}: "

        # Prompt the user for value input
        while origin.run_loop:
            valid_type = "Number"
            temp = input(f"Enter the value for \"{temp}\" should be a {valid_type}: ")
            origin.run_loop = True if temp not in origin.db_interface.display.exit_commands else False

        query += f"WHERE {find} = {temp}"

        return query
    
    @staticmethod
    def help():
        print("Help")
        return True