"""

"""

from sqlite3 import Connection
import MuscleGroup
import MuscleGroups

class AddMuscleGroup:
    def __init__(self, connection: Connection, muscle_groups: MuscleGroups) -> None:
        self.muscle_group = None
        self.connection = connection
        self.cur = self.connection.cursor()
        self.muscle_groups = muscle_groups
        self.workout = None

    def set_muscle_group(self):
        self.muscle_group = input("What is the name of the muscle group? ")
        value = (self.muscle_group)
        self.cur.execute("""CREATE TABLE IF NOT EXISTS ? ([workout_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
            [workout_name] TEXT, [workout_weight_upper_range] INTEGER, 
            [workout_weight_lower_range] INTEGER, [workout_weight_range] TEXT)""", value)
        return self.muscle_group
    
    def set_workouts(self):
        add_workout = True
        while add_workout == True :
            self.workout = str(input("What is the name of the workout? "))
            values = (self.muscle_group, self.workout)
            self.cur.execute("INSERT INTO ? (workout_name) VALUES (?)", values)
            add_new_workout = input("Would you like to add another workout? (Yes/No)")
            
            if add_new_workout.title() == "No" :
                add_workout = False
            
            else :
                add_workout = True
    
    def create_muscle_class(self):
        value = (self.muscle_group)
        self.cur.execute("SELECT workout_name FROM ? ", value)
        workouts = self.cur.fetchall()
        new_muscle_group = MuscleGroup(self.muscle_group, workouts, self.connection)
        self.muscle_groups.add_muscle_groups(new_muscle_group)
    
