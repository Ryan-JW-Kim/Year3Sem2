from student import *
from staff import *
from display import *
from db_manager import *


def main():

    # Introduct Program
    msg = "Welcome to the Library Management System..."
    print(msg)

    # Select user type
    user = Display.prompt_user_type()

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
    
    user = Staff()

    user.prompt_command()

    print(user.available_commands)

if __name__ == "__main__":

    test_main()