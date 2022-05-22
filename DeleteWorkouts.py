"""

"""

from sqlite3 import Connection


class DeleteWorkouts:
    def __init__(self, connection: Connection) -> None:
        self.conn = connection
        self.cur = self.conn.cursor()
    
    def delete_workouts(self, muscle_group_list: list):
        delete_workout = True
        while delete_workout == True:
            muscle_group = input("What is the muscle group that you would like to delete from? ")
            workout = input("What is the workout you would like to delete? ")
            
            if muscle_group.title() in muscle_group_list :
                values = (muscle_group, workout)
                self.cursor.execute("SELECT * FROM ?")
                workouts = self.cursor.fetchall()

                if workout.title() in workouts :
                    self.cursor.execute("DELETE FROM ? WHERE workout_name LIKE %?%")
                
                else :
                    print("ERROR: Workout does not exist")
                    delete_workout = True
            else :
                print("ERROR: Muscle Group does not exist")
                delete_workout = True
            
            self.connection.commit()
