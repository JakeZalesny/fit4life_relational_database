"""


"""



from sqlite3 import Connection


class MuscleGroup :
    def __init__(self, name: str, workouts: str, connection: Connection, cursor) -> None:
        self.name = name
        self.workouts = workouts
        self.connection = connection
    
    def get_name(self) -> str :
        return self.name
    
    def get_workouts(self) -> str :
        return self.workouts

    def add_workouts(self) -> None :
        add_workout = True
        while add_workout == True:

            muscle_group = input("What is the muscle group that you would like to add to") 
            workout = input("What is the workout you would like to add")