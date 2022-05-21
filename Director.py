import Constants
from CreateConnection import CreateConnection, CreateDatabase
from CreateDefaultWorkouts import CreateDefaultWorkouts
from MuscleGroup import MuscleGroup
from MuscleGroups import MuscleGroups
"""

"""

class Director: 
    def __init__(self) -> None :
        self.CREATE_CONNECTION = CreateConnection()
        self._CONNECTION = CreateConnection.create_connection()
        self._DEFAULT_WORKOUTS = CreateDefaultWorkouts(self._CONNECTION)
        self._MUSCLE_GROUPS = MuscleGroups()
        
        self._SHOULDERS = MuscleGroup("Shoulders", Constants.DEFAULT_WORKOUTS["Shoulders"], self._CONNECTION)
        self._CHEST = MuscleGroup("Chest", Constants.DEFAULT_WORKOUTS["Chest"], self._CONNECTION)
        self._LEGS = MuscleGroup("Legs", Constants.DEFAULT_WORKOUTS["Legs"], self._CONNECTION)
        self._BACK = MuscleGroup("Back", Constants.DEFAULT_WORKOUTS["Back"], self._CONNECTION)
        self._ABS = MuscleGroup("Abs", Constants.DEFAULT_WORKOUTS["Abs"], self._CONNECTION)
        self._BICEPS = MuscleGroup("Biceps", Constants.DEFAULT_WORKOUTS["Biceps"], self._CONNECTION)
        self._TRICEPS = MuscleGroup("Triceps", Constants.DEFAULT_WORKOUTS["Triceps"], self._CONNECTION)

        self._MUSCLE_GROUPS.add_muscle_groups(self._SHOULDERS)
        self._MUSCLE_GROUPS.add_muscle_groups(self._CHEST)
        self._MUSCLE_GROUPS.add_muscle_groups(self._LEGS)
        self._MUSCLE_GROUPS.add_muscle_groups(self._BACK)
        self._MUSCLE_GROUPS.add_muscle_groups(self._ABS)
        self._MUSCLE_GROUPS.add_muscle_groups(self._BICEPS)
        self._MUSCLE_GROUPS.add_muscle_groups(self._TRICEPS)

        self._LIST_OF_MUSCLES = self._MUSCLE_GROUPS.get_list_of_groups()

        for muscle in self._LIST_OF_MUSCLES :
            self._DEFAULT_WORKOUTS.create_table(muscle)
            for workout in muscle.get_workouts() :
                self._DEFAULT_WORKOUTS.add_default_workouts(workout, muscle)

         

        
        self._CONNECTION.close()
    
    def direct() :
        pass
