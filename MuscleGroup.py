"""


"""



from sqlite3 import Connection


class MuscleGroup :
    def __init__(self, name: str, workouts: list, connection: Connection) -> None:
        self.name = name
        self.workouts = workouts
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def get_name(self) -> str :
        return self.name
    
    def get_workouts(self) -> str :
        return self.workouts
