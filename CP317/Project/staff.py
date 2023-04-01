from Utils import text
from db_manager import *
from display import *

class Staff:

    @staticmethod
    def checkout_book_id(id: int):
        query = ""

        # Create Query for certain book via input()

        result = Database.execute_query(query)
        Display.present_query(result, usertype="Staff")


    @staticmethod
    def get_user_info_id(id: int):
        
        query = ""

        # Create query for certain user via input()

        result = Database.execute_query(query)
        Display.present_query(result, usertype="Staff")