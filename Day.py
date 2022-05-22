"""

"""
from sqlite3 import Connection
import MuscleGroup
class Day:
    def __init__(self, day: str, connection: Connection) -> None:
        self.muscle_group = None
        self.day = day
        self.conn = connection
        self.cur = self.conn.cursor()
        self.all_workouts = []
    
    def get_name(self):
        return self.day

    def get_muscle_group(self):
        self.muscle_group = input(f"What muscle do you want to work today({self.day.title()}? ")
    
    def get_all_workouts(self, muscle_group_list: list):
        if self.muscle_group in muscle_group_list :
            value = (self.muscle_group)
            self.cur.execute("SELECT * FROM ?", value)
            self.all_workouts = self.cur.fetchall()
        
        return self.all_workouts
       
