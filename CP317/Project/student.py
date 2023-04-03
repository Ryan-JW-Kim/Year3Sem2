from display import *
from db_manager import *

class Student:

    db_interface = Database

    @staticmethod
    def find_book():
        result = Student.db_interface.get_book_id()
        Display.present_query(result, usertype="Student")

    def search_for_books():
        result = Student.db_interface.search_book()
        Display.present_query(result, usertype="Student")

    def reserve_book():
        result = Student.db_interface.reserve_book_id()
        Display.present_query(result, usertype="Student")

    @staticmethod
    def is_valid_cmd(cmd: str):
        pass

    @staticmethod
    def available_commands():
        pass