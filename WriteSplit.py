"""

"""
from sqlite3 import Connection
import Day
import random
class WriteSplit:
    def __init__(self, connection: Connection) -> None:
        self.monday = Day("Monday", connection)
        self.tuesday = Day("Tuesday", connection)
        self.wednesday = Day("Wednesday", connection)
        self.thursday = Day("Thursday", connection)
        self.friday = Day("Friday", connection)
        self.saturday = Day("Saturday", connection)
        self.sunday = Day("Sunday", connection)
        self.workouts_per_day = {}
        self.list_of_days = [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday, self.sunday]
        self.conn = connection
        self.cur = self.conn.cursor()


    def get_muscle_groups(self, list_of_muscles: list):
        counter = 0 
        for day in self.list_of_days:
            muscle_group = day.get_muscle_group()
            all_workouts = day.get_all_workouts(list_of_muscles)
            self.workouts_per_day[self.list_of_days[counter].get_name()] = all_workouts
            counter += 1
    
    def write_split(self):
        for day in self.list_of_days:
            name = day.get_name()
            workout_1 = self.workouts_per_day[name][random.randint(0, len(self.workouts_per_day[name]))]
