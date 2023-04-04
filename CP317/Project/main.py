from display import Display
from db_manager import Database


def main():

    # Introduct Program
    msg = "Welcome to the Library Management System..."
    print(msg)

    # Select user type
    user = Display.prompt_user_type(Database)

    # Prompt for input
    user.prompt_command()

    # While the user indicates the loop should run
    while user.run_loop:
        
        # While the user has failed to provide a valid command (and has not quit)
        while user.has_no_command:
            user.prompt_command()

        # Complete stored command
        user.do()

def test_main():
    
    user = Display.prompt_user_type(Database)
    user.prompt_command()
    
    while user.run_loop:
        while user.has_no_command and user.run_loop:
            user.prompt_command()
        
        if user.has_no_command is False:
            user.do()
        

if __name__ == "__main__":

    test_main()