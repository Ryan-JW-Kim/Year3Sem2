
class Display:
    valid_usertype = ["Staff", "Student"]

    @staticmethod
    def help():
        pass

    @staticmethod
    def present_query(data, usertype="Student"):
        
        if usertype not in Display.valid_usertype:
            raise ValueError("Invalid usertype for presentation")
        
        if usertype == "Staff":
            
            if data["type"] == "Book Info":
                pass
            
            else:
                pass
            
        elif usertype == "Student":
            
            if data["type"] == "Book Info":
                pass

            else:
                pass