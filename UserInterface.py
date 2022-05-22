"""

"""

class UserInterface: 
    def __init__(self) -> None:
        self._menu = """
        1. Write Split
        2. Add Muscle Group
        3. Add Workout
        4. Delete Workout
        5. Modify Maxes
        6. Quit
        """

    def get_input(self) -> int:
        user_choice = int(input(self._menu))
        return user_choice
    
