from student import Student
from staff import Staff

class Display:

    valid_user_types = ["student", "staff"]
    exit_commands = ["quit", "exit"]

    @staticmethod
    def prompt_user_type(db_interface):

        prompt = "\nAre you a \"student\" or \"staff\" member: "
        user_type = input(prompt)

        while user_type not in Display.exit_commands:

            if user_type not in Display.valid_user_types or user_type in Display.exit_commands:
                print("Invalid user type. Please try again.")
                user_type = input(prompt)

            else:
                break
        
        print("\n")

        if user_type == "student":
            return Student(db_interface)
        
        elif user_type == "staff":
            return Staff(db_interface)
        
    @staticmethod
    def prompt_for_query(params: dict, origin, query, assemble=True):

        expect = query.count("%s")    

        if expect != len(params):
            print("Error: parameter mismatch.")
            return False
    
        print(f"Please enter values for command: ")

        values = []
        for param in params:
            temp = input(f"  - {param['Display Name']} ({param['Type']}): ")
            
            origin.run_loop = True if temp not in origin.db_interface.display.exit_commands else False
            
            if origin.run_loop is False:
                return False

            values.append(temp)


        return query % tuple(values) if assemble else values
    
    @staticmethod
    def help():
        print("Help")
        return True