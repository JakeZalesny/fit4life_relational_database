import sqlite3
from sqlite3 import Error

class CreateDatabase :
    def __init__(self, database_file : str) -> None:
        self.database_file = database_file
        self.conn = None

    def create_database(self):
        try :
            self.conn = sqlite3.connect(self.database_file)
        
        except Error as e :
            print(e)
        
        finally :
            if self.conn :
                self.conn.close()
        return self.conn
    
