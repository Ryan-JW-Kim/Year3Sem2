import mysql.connector
from display import Display

"""
books
 - id (unique id of book)
 - title (title of book)
 - author (author of book)
 - year (year of publication)
 - quantity (number of copies of book)                |
 - reserved (number of copies of book reserved)       |
 - taken_copies (number of copies of book taken out)  | -> all four are related values.... quantity = reserved + taken_copies + available
 - available (number of copies of book available)     |

user
 - id (unique id of user)
 - name (name of user)
 - type (student or staff)
 - books (list of books checked out by user)
 - reserved (list of books reserved by user)
 - overdue (list of books overdue by user)
 - fines (total amount of fines owed by user)                              |
 - max_fines (max amount of fines owed by user)                            | -> all three are related values.... not allowed if fines >= max_fines
 - is_allowed (boolean indicating if user is allowed to check out books)   |

"""

class Database:
    active_connector = None
    display = Display

    def __init__(self, user_type: str):
        
        self.user_type = user_type

        host = "localhost"
        user = "root"
        password = "password"

        Database.active_connector = mysql.connector.connect(host=host, user=user, password=password, database="library")

    @staticmethod
    def user_has_authority(origin, cmd: str):
        
        authorities = {"Get Book": ["student", "staff"],
                       "Add Book": ["staff"],
                       "Delete Book": ["staff"],
                       "Reserve Book": ["student", "staff"],
                       "Checkout Book": ["staff"]}
        

        return True if origin.type in authorities[cmd] else False

    @staticmethod
    def execute_query(query: str, fetch=False):
        # mycursor = Database.active_connector.cursor()
        # mycursor.execute(query)
        # return mycuros.fetchall() if fetch else True

        print(f"\n    Executing query: {query}\n")

    @staticmethod
    def valid_user_type(user_type: str):
        
        if user_type not in ["student", "staff"]:
            return False
        
        return True

    @staticmethod
    def get_book(origin):

        if Database.user_has_authority(origin, "Get Book") is False:
            return False
        
        book = Database.query_book_info(origin)
        
        if book:
            return True

        return False
    
    @staticmethod
    def query_book_info(origin, id=None):
        if Database.user_has_authority(origin, "Get Book") is False:
            return False
        
        if id is None:
            params = [{"Display Name": "Book ID",
                   "Type": "Number"}]
            
            query_template = "SELECT * FROM books WHERE id=%s" 
            query = Display.prompt_for_query(params, origin, query_template)

            if query:
                return Database.execute_query(query)
                    
        else:
            query = f"SELECT * FROM books WHERE id={id}"
            return Database.execute_query(query)

    @staticmethod
    def reserve_book(origin, id=None):

        if Database.user_has_authority(origin, "Reserve Book") is False:
            return False
        
        book = Database.query_book_info(origin)

        if book["Available"]:
            
            # Update status of reservation
            query_template = f"UPDATE books \nSET reserved=1 \nWHERE id={book['ID']}"
            Database.execute_query(query_template)

            # Update counter for total number of available books
            query_template = f"UPDATE users \nSET available={book['available']-1} \nWHERE id={origin.id}"
            Database.execute_query(query_template)

            return True
        
        else:
            print(f"Sorry book is not available.")
    
        return False

    @staticmethod
    def add_book(origin):
        if Database.user_has_authority(origin, "Add Book") is False:
            return False
        
        params = [{"Display Name": "Title", "Type": "String"},
                  {"Display Name": "Author", "Type": "String"},
                  {"Display Name": "Year", "Type": "Number"},
                  {"Display Name": "Quantity", "Type": "Number"}]
        
        query_template = ""
        
        values = Display.prompt_for_query(params, origin, query_template, assemble=False)
        
        available = values[3]
        reserved = 0
        taken_copies = 0
        
        query = f"INSERT INTO books (title, author, year, quantity, available, reserved, taken_copies) VALUES ({values[0]}, {values[1]}, {values[2]}, {values[3]}, {available}, {reserved}, {taken_copies})"
        
        if Database.execute_query(query):
            return True
    
        return False
    
    @staticmethod
    def add_user(origin):
        if Database.user_has_authority(origin, "Add User") is False:
            return False
        
        params = [{"Display Name": "Name", "Type": "String"},
                  {"Display Name": "Type", "Type": "String"}]
        
        values = Display.prompt_for_query(params, origin, assemble=False)

        books = []
        reserved = []
        overdue = []
        fines = 0
        max_fines = 100
        is_allowed = True

        query = f"INSERT INTO users (name, type, books, reserved, overdue, fines, max_fines, is_allowed) VALUES ({values[0]}, {values[1]}, {books}, {reserved}, {overdue}, {fines}, {max_fines}, {is_allowed})"

        if Database.execute_query(query):
            return True
        
        return False