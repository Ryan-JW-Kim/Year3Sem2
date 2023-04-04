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
        
        authorities = {"Get Books": ["student", "staff"],
                       "Add Book": ["staff"],
                       "Delete Book": ["staff"],
                       "Update Book": ["staff"],
                       "Reserve Book": ["student", "staff"],
                       "Checkout Book": ["staff"],
                       "Search Book": ["student", "staff"]}
        
        return True if origin.type in authorities[cmd] else False

    @staticmethod
    def execute_query(query: str):
        mycursor = Database.active_connector.cursor()
        mycursor.execute(query)
        return True

    @staticmethod
    def valid_user_type(user_type: str):
        
        if user_type not in ["student", "staff"]:
            return False
        
        return True

    @staticmethod
    def get_books(origin):

        if Database.user_has_authority(origin, "Get Books") is False:
            return False
        
        params = [{"Display Name": "id", 
                   "Type": "(Number)",
                   "Action": "Get book"}]

        query_template = "SELECT * FROM books WHERE id = %s" 
        query = Display.prompt_for_query(params, query_template, origin)

        Database.execute_query(query)

        return True
    
    @staticmethod
    def search_book(origin):
        if Database.user_has_authority(origin, "Search Book") is False:
            return False
        query = ""
    
    @staticmethod
    def reserve_book(origin):
        if Database.user_has_authority(origin, "Reserve Book") is False:
            return False
        query = ""

    @staticmethod
    def add_book(origin):
        if Database.user_has_authority(origin, "Add Book") is False:
            return False
        
        print("adding")
        query = ""
        return False
    
    @staticmethod
    def add_user(origin):
        if Database.user_has_authority(origin, "Add User") is False:
            return False
        query = ""
        return False