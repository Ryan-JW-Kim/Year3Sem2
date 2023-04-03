from db_manager import *
from display import *

class Staff:

    db_interface = Database

    @staticmethod
    def checkout_book_id(id: int):

        # Prompt for book id

        # is valid book id

        # is book available

        # is user allowed to checkout

        # checkout book

        query = ""
        # Create Query for certain book via input()

        result = Staff.db_interface.execute_query(query)
        Display.present_query(result, usertype="Staff")


    @staticmethod
    def get_user_info_id(id: int):
        
        # Prompt for user id

        # is valid user id

        # get user info

        query = ""

        # Create query for certain user via input()

        result = Staff.db_interface.execute_query(query)
        Display.present_query(result, usertype="Staff")

    @staticmethod
    def is_valid_cmd(cmd: str):
        pass

    @staticmethod
    def available_commands():
        pass
