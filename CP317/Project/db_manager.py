import mysql.connector


class Book:
    def __init__(self, id: int, name: str, author: str, year: int, available: bool):
        self.id = id
        self.name = name
        self.author = author
        self.year = year
        self.available = available


class Database:
    valid_book_fields = ["id", "name", "author", "year", "available"]

    active_connector = None

    def __init__(self, user_type: str):
        
        self.user_type = user_type

        host = "localhost"
        user = "root"
        password = "password"

        Database.active_connector = mysql.connector(host=host, user=user, password=password, database="library")

    @staticmethod
    def get_books(search_params: list):
        # Prompt for valid parameters
        msg = "Enter search parameter (author, genre, year)"

        prompt = ""
        cmd = input(prompt)

        # Create query for certain book via input()

        # Execute query
        query = ""

        result = Book.execute_query(query)
        return result

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

    @staticmethod
    def valid_user_type(user_type: str):
        pass

    @staticmethod
    def set_user(user_type: str):
        pass

    @staticmethod
    def initilize_database_file():
        if Database.active_connector is None:
            raise ValueError("No active connector")
        
        mycursor = Database.active_connector.cursor()

        mycursor.execute("CREATE DATABASE library")

        # Double check if tables are right
        mycursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), author VARCHAR(255), year INT, available BOOLEAN)")        
        mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), type VARCHAR(255))")
        mycursor.execute("CREATE TABLE reservations (id INT AUTO_INCREMENT PRIMARY KEY, book_id INT, user_id INT, FOREIGN KEY (book_id) REFERENCES books(id), FOREIGN KEY (user_id) REFERENCES users(id))")


    @staticmethod
    def close_database_file():
        if Database.active_connector is None:
            raise ValueError("No active connector")
        
        Database.active_connector.close()
    
    @staticmethod
    def fill_database_test():
        if Database.active_connector is None:
            raise ValueError("No active connector")
        
        # Create test data as dict

        # Create test users as dict

        # Create test reservations as dict

        # Add test data to database

