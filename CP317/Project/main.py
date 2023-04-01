from Utils import text
from student import *
from staff import *
from display import *
from report import *
from db_manager import *


def main():

    print(text["First line"])
    cmd = input(text["Input Prompt"])
    
    while cmd not in text["Exit Command"]:
        
        if cmd in text["Student Command"]:
            Student.perform_command(cmd)

        elif cmd in text["Staff Command"]:
            Staff.perform_command(cmd)

        elif cmd in text["Display Command"]:
            Display.perform_command(cmd)

        elif cmd in text["Help Command"]:
            Help.print_help()

        else:
            Help.print_invalid_command()

        cmd = input(text["Input Prompt"])

if __name__ == "__main__":
    main()