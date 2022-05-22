"""

"""
import MuscleGroup

class MuscleGroups :
    def __init__(self) -> None:
        self._list_of_groups : list = []
    
    def add_muscle_groups(self, muscle_group: MuscleGroup) :
        print(muscle_group.get_name())
        self._list_of_groups.append(muscle_group)
    
    def get_list_of_groups(self) -> list :
        return self._list_of_groups