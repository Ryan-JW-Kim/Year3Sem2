import mysql.connector
from display import Display

class Database:
    active_connector = None
    user_authorities = {"student": ["Get Book", "Reserve Book"],
                        "staff": ["Get Book", "Add Book", "Delete Book", "Reserve Book", "Checkout Book"]}

    display = Display

    def __init__(self):
        host = "localhost"
        user = "root"
        password = "password"
        
        Database.active_connector = mysql.connector.connect(host=host, user=user, password=password, database="library")

    @staticmethod
    def user_has_authority(origin, cmd: str):

        if origin.type in Database.user_authorities:
            return True if cmd in Database.user_authorities[origin.type] else False

        return True if origin.type in Database.user_authorities[cmd] else False

    @staticmethod
    def execute_query(query, fetch=False, val=None):

        if type(query) is str:
            print(f"\n    Executing query: {query}")
            mycursor = Database.active_connector.cursor()

            if val is not None:
                mycursor.execute(query, val)
            
            else:
                mycursor.execute(query)

            print(f"    Completed query: {query}\n")
            
            return mycursor.fetchall() if fetch else True
            
        else:
            results = []
            mycursor = Database.active_connector.cursor()

            for q in query:
                print(f"\n    Executing query: {q}\n")
                mycursor.execute(q)
                results.append(mycursor.fetchall() if fetch else True)
                print(f"\n    Completed query: {q}\n")
            return results
        
    @staticmethod
    def valid_user_type(user_type: str):  
        if user_type not in Database.user_authorities:
            return False
        
        return True

    @staticmethod
    def get_book(origin):

        if Database.user_has_authority(origin, "Get Book") is False:
            return False
        
        book = Database.query_book_info(origin)

        if not book:
            return False

        print(f"Book Found .... \"{book['Title']}\" by {book['Author']} ({book['Year']}) --- \"{book['Available']}\" copies available.")

        return True
    
    @staticmethod
    def query_book_info(origin, id=None):
        if Database.user_has_authority(origin, "Get Book") is False:
            return False
        
        if id is None:
            params = [{"Display Name": "Book ID",
                   "Type": "Number"}]
            
            query_template = "SELECT * FROM books WHERE book_id=%s" 
            query = Display.prompt_for_query(params, origin, query_template)

            if query:
                temp = Database.execute_query(query, fetch=True)
                if len(temp) == 0:
                    print("Book not found")
                    return False
                
                else:
                    temp = list(temp[0])

                return {"ID": temp[0], "Title": temp[1], "Author": temp[2], "Year": int(temp[3]), "Quantity": int(temp[4]), "Reserved": int(temp[5]), "Taken Copies": int(temp[6]), "Available": int(temp[7])}
                    
        else:
            query = f"SELECT * FROM books WHERE book_id={id}"
            temp = Database.execute_query(query, fetch=True)
            if len(temp) == 0:
                print("Book not found")
                return False
            else:
                temp = list(temp[0])
            return {"ID": temp[0], "Title": temp[1], "Author": temp[2], "Year": int(temp[3]), "Quantity": int(temp[4]), "Reserved": int(temp[5]), "Taken Copies": int(temp[6]), "Available": int(temp[7])}

    @staticmethod
    def reserve_book(origin, id=None):

        if Database.user_has_authority(origin, "Reserve Book") is False:
            return False
        
        book = Database.query_book_info(origin)
        
        if not book:
            return False

        if book["Available"] > 0:
            
            # Update status of reservation
            query = f"UPDATE books SET reserved={book['Reserved']+1}, available={book['Available']-1} WHERE book_id={book['ID']}"

            Database.execute_query(query)

            return True
        
        else:
            print(f"Sorry book is not available.")
    
        return False

    @staticmethod
    def checkout_book(origin):

        if Database.user_has_authority(origin, "Checkout Book") is False:
            return False
        
        book = Database.query_book_info(origin)
        print(book)

        if not book:
            return False

        if book["Available"] > 0:
            
            # Update status of reservation
            query = f"UPDATE books SET taken_copies={book['Taken Copies']+1}, available={book['Available']-1} WHERE book_id={book['ID']}"

            Database.execute_query(query)

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
        
        query = f"INSERT INTO books (title, author, year, quantity, available, reserved, taken_copies) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (values[0], values[1], values[2], values[3], available, reserved, taken_copies)
        
        if Database.execute_query(query, val=val):
            return True
    
        return False
    
    @staticmethod
    def delete_book(origin): 
        if Database.user_has_authority(origin, "Add Book") is False:
            return False

        book = Database.query_book_info(origin)

        if not book:
            return False
    
        confirm = Display.prompt_for_confirmation(f"Are you sure you want to remove {book['Title']} by {book['Author']} ({book['Year']})?")

        if confirm is False:
            return False
        
        query = f"DELETE FROM books WHERE book_id={book['ID']}"

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