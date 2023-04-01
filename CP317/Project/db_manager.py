
class Book:
    def __init__(self, id: int, name: str, author: str, year: int, available: bool):
        self.id = id
        self.name = name
        self.author = author
        self.year = year
        self.available = available


class Database:
    valid_book_fields = ["id", "name", "author", "year", "available"]

    @staticmethod
    def get_books(search_params: list):
        pass

    @staticmethod
    def get_book(find_from: str):
        if find_from not in Database.valid_book_fields:
            raise ValueError("Invalid field for book search")
        
        pass

    @staticmethod
    def reserve_book(find_from: str):
        if find_from not in Database.valid_book_fields:
            raise ValueError("Invalid field for book search")
        
        pass

    @staticmethod
    def execute_query(query: str):
        pass