from student import *
from staff import *
from display import *
from db_manager import *


def main():

    # Introduct Program
    msg = "Hello intro"
    print(msg)

    # Select user type
    user = Student
    msg = "Select user type"
    temp = input(msg)

    Database(user)

    if False:
        Database.initilize_database_file()
        Database.fill_database_test()

    # while is not valid user type
    while not Database.valid_user_type(temp):
        break
        # Prompt for user type
    
    user = Database.set_user(temp)
    
    # Prompt for input
    msg = user.available_commands()
    cmd = input(msg)

    while user.is_valid_cmd(cmd):
        pass
        # Inform user of valid commands

        # Prompt for input

        # Execute command, break, or pass

    Database.close_database_file()

if __name__ == "__main__":

    main()
