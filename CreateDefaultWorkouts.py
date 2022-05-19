"""


"""



import sqlite3
from sqlite3 import Connection
import Constants

class CreateDefaultWorkouts :
    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.conn = connection.cursor()
    
    def create_tables(self) :
        
        for muscle_group in Constants.DEFAULT_MUSCLE_GROUPS :
            value = (muscle_group)
            self.conn.execute("""CREATE TABLE IF NOT EXISTS ? ([workout_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
            [workout_name] TEXT, [workout_weight_upper_range] INTEGER, [workout_weight_lower_range] INTEGER, [workout_weight_range] TEXT
            """, value)
        self.connection.commit()
    
    def add_default_workouts(self):
        i = 0
        for muscle_group in Constants.DEFAULT_MUSCLE_GROUPS : 
            values = (muscle_group, Constants.DEFAULT_WORKOUTS[muscle_group][i])
            self.conn.execute("INSERT INTO ? VALUES( , ?, 0, 0, null)", values)
        
        self.connection.commit()