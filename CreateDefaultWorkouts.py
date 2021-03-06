"""


"""



import sqlite3
from sqlite3 import Connection
import Constants
from MuscleGroup import MuscleGroup

class CreateDefaultWorkouts :
    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.conn = connection.cursor()
    
    def create_table(self, muscle_group: MuscleGroup) :
            value = (muscle_group.get_name())
            self.conn.execute("""CREATE TABLE IF NOT EXISTS "{}" ([workout_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
            [workout_name] TEXT, [workout_weight_upper_range] INTEGER, [workout_weight_lower_range] INTEGER, [workout_weight_range] TEXT)
            """.format(value))
            print(muscle_group)
            self.connection.commit()
    
    def add_default_workouts(self, workouts: MuscleGroup, muscle_group: MuscleGroup):

        values = (muscle_group.get_name(), workouts)
        self.conn.execute("INSERT INTO '{}' (workout_name) VALUES('{}')".format(values[0], values[1]))
        
        self.connection.commit()