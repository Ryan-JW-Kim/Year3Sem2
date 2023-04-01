from display import *
from db_manager import *

class Student:

    @staticmethod
    def find_book():
        result = Database.get_book_id()
        Display.present_query(result, usertype="Student")

    def search_for_books():
        result = Database.search_book()
        Display.present_query(result, usertype="Student")

    def reserve_book():
        result = Database.reserve_book_id()
        Display.present_query(result, usertype="Student")