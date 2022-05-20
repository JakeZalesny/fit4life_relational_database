import sqlite3
from sqlite3 import Error

class CreateConnection:
    def __init__(self, database_file : str) -> None:
        self.database_file = database_file
        self.conn = None
        self.cur = None

    def create_connection(self):
        try :
            self.conn = sqlite3.connect(self.database_file)
        
        except Error as e :
            print(e)
        
        
        return self.conn
    
