"""

"""
from sqlite3 import Connection
import Day
import random
class WriteSplit:
    def __init__(self, connection: Connection, day: Day) -> None:
        self.day = day
        self.monday = day.set_name("Monday")
        self.tuesday = day.set_name("Tuesday")
        self.wednesday = day.set_name("Wednesday")
        self.thursday = day.set_name("Thursday")
        self.friday = day.set_name("Friday")
        self.saturday = day.set_name("Saturday")
        self.sunday = day.set_name("Sunday")
        self.workouts_per_day = {}
        self.list_of_days = [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday, self.sunday]
        self.conn = connection
        self.cur = self.conn.cursor()


    def get_muscle_groups(self, list_of_muscles: list):
        muscle_group = self.day.set_muscle_group()
        all_workouts = self.day.get_all_workouts(list_of_muscles)
        for i in self.workouts_per_day:
            self.workouts_per_day[self.list_of_days[i]] = all_workouts
    
    def write_split(self):
        for day in self.list_of_days:
            name = day.get_name()
            workout_1 = self.workouts_per_day[name][random.randint(0, len(self.workouts_per_day[name]))]
            workout_2 = self.workouts_per_day[name][random.randint(0, len(self.workouts_per_day[name]))]
            workout_3 = self.workouts_per_day[name][random.randint(0, len(self.workouts_per_day[name]))]
            workout_4 = self.workouts_per_day[name][random.randint(0, len(self.workouts_per_day[name]))]
            workout_5 = self.workouts_per_day[name][random.randint(0, len(self.workouts_per_day[name]))]
            
            print(name)
            print()
            print(workout_1)
            print(workout_2)
            print(workout_3)
            print(workout_4)
            print(workout_5)
            print()
