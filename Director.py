import Constants
from CreateDatabase import CreateDatabase
from CreateDefaultWorkouts import CreateDefaultWorkouts
"""

"""

class Director: 
    def __init__(self) -> None :
        self.CREATE_DATABASE = CreateDatabase()
        self._CONNECTION = CreateDatabase.create_database()
        self._DEFAULT_WORKOUTS = CreateDefaultWorkouts(self._CONNECTION)
    
    def direct() :
        pass
