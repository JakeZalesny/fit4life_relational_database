"""

"""

class UserInterface: 
    def __init__(self) -> None:
        self._menu = """
        1. Write Split
        2. See Previous Splits 
        3. Add Muscle Group
        4. Add Workout
        5. Delete Workout
        6. Modify Maxes
        7. Check Current Workouts
        8. Quit
        """

    def get_input(self) -> int:
        user_choice = int(input(self._menu))
        return user_choice
    
