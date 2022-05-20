import Constants
from CreateConnection import CreateConnection, CreateDatabase
from CreateDefaultWorkouts import CreateDefaultWorkouts
"""

"""

class Director: 
    def __init__(self) -> None :
        self.CREATE_CONNECTION = CreateConnection()
        self._CONNECTION = CreateConnection.create_connection()
        self._DEFAULT_WORKOUTS = CreateDefaultWorkouts(self._CONNECTION)
        self._CONNECTION.close()
    
    def direct() :
        pass
