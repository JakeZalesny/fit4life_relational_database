"""

"""
from sqlite3 import Connection
import MuscleGroup
class Day:
    def __init__(self, connection: Connection) -> None:
        self.muscle_group = None
        self.conn = connection
        self.name = None
        self.cur = self.conn.cursor()
        self.all_workouts = []
    
    def set_name(self, name):
        self.name = name
        return self.name

    def get_name(self):
        return self.name

    def set_muscle_group(self):
        self.muscle_group = input(f"What muscle do you want to work today({self.day.title()}? ")
    
    def get_muscle_group(self):
        return self.muscle_group
    
    def get_all_workouts(self, muscle_group_list: list):
        if self.muscle_group in muscle_group_list :
            value = (self.muscle_group)
            self.cur.execute("SELECT * FROM ?", value)
            self.all_workouts = self.cur.fetchall()
        
        return self.all_workouts
       
