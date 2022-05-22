from ast import While
from AddMuscleGroup import AddMuscleGroup
from AddWorkouts import AddWorkouts
import Constants
from CreateConnection import CreateConnection
from CreateDefaultWorkouts import CreateDefaultWorkouts
from DeleteWorkouts import DeleteWorkouts
from Maxes import Maxes
from MuscleGroup import MuscleGroup
from MuscleGroups import MuscleGroups
from UserInterface import UserInterface
from WriteSplit import WriteSplit
from Day import Day

"""

"""

class Director: 
    def __init__(self) -> None :
        self.CREATE_CONNECTION = CreateConnection(Constants.DATABASE_FILE)
        self._CONNECTION = self.CREATE_CONNECTION.create_connection()
        self._DEFAULT_WORKOUTS = CreateDefaultWorkouts(self._CONNECTION)
        self._MUSCLE_GROUPS = MuscleGroups()
        self._DAY = Day(self._CONNECTION )
        self._MAXES = Maxes(self._CONNECTION)
        self._ADD_WORKOUTS = AddWorkouts(self._CONNECTION)
        self._DELETE_WORKOUTS = DeleteWorkouts(self._CONNECTION)
        self._ADD_MUSCLE_GROUP = AddMuscleGroup(self._CONNECTION, self._MUSCLE_GROUPS)
        self._WRITE_SPLIT = WriteSplit(self._CONNECTION, self._DAY)
        self._UI = UserInterface()
        
        
        self._SHOULDERS = MuscleGroup("Shoulders", Constants.DEFAULT_WORKOUTS["Shoulders"], self._CONNECTION)
        self._CHEST = MuscleGroup("Chest", Constants.DEFAULT_WORKOUTS["Chest"], self._CONNECTION)
        self._LEGS = MuscleGroup("Legs", Constants.DEFAULT_WORKOUTS["Legs"], self._CONNECTION)
        self._BACK = MuscleGroup("Back", Constants.DEFAULT_WORKOUTS["Back"], self._CONNECTION)
        self._ABS = MuscleGroup("Abs", Constants.DEFAULT_WORKOUTS["Abs"], self._CONNECTION)
        self._BICEPS = MuscleGroup("Biceps", Constants.DEFAULT_WORKOUTS["Biceps"], self._CONNECTION)
        self._TRICEPS = MuscleGroup("Triceps", Constants.DEFAULT_WORKOUTS["Triceps"], self._CONNECTION)

    
    def direct(self) :
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
            current_workouts = self.CREATE_CONNECTION.check_status(muscle)
            for workout in muscle.get_workouts() :
                if workout not in current_workouts :
                    self._DEFAULT_WORKOUTS.add_default_workouts(workout, muscle)
        
        self._MAXES.create_maxes_table()
        self._MAXES.set_maxes()
        user_choice = 0
        
        while user_choice != 6 :
           user_choice = self._UI.get_input()
           match user_choice :
                case 1 :
                   self._WRITE_SPLIT.get_muscle_groups(self._LIST_OF_MUSCLES)
                   self._WRITE_SPLIT.write_split()
                   break
                
                case 2 :
                    self._ADD_MUSCLE_GROUP.set_muscle_group()
                    self._ADD_MUSCLE_GROUP.set_workouts()
                    self._ADD_MUSCLE_GROUP.create_muscle_class()
                    break

                case 3 :
                    self._ADD_WORKOUTS.add_workout(self._LIST_OF_MUSCLES)
                    break

                case 4 :
                    self._DELETE_WORKOUTS.delete_workouts(self._LIST_OF_MUSCLES)
                    break
                
                case 5 :
                    self._MAXES.get_modification()
                    self._MAXES.modify_max()
                    break
                
                case 6 :
                    self._CONNECTION.close()
                    quit()
