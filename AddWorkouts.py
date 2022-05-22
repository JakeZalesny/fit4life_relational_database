"""

"""




from sqlite3 import Connection


class AddWorkouts:
    def __init__(self, connection: Connection) -> None:
        self.conn = connection
        self.cur = self.conn.cursor()

    def add_workout(self, muscle_group_list: list):
        add_workout = True
        while add_workout == True:
            muscle_group = input("What is the muscle group that you would like to add to? ") 
            workout = input("What is the workout you would like to add? ")
            
            if muscle_group.title() in muscle_group_list :
                values = (muscle_group, workout)
                self.cur.execute("""SELECT * FROM ? """, values)
                workouts = self.cur.fetchall()
                
                if workout.title() not in workouts :
                    self.cur.execute("""INSERT INTO ? (workout_name) VALUES(?) """, values)
                
                else :
                    print("ERROR: Workout already exists")
                    add_workout = True
            
            
            else :
                print("ERROR: Muscle Group does not exist")
                add_workout = True
            
            add_new_workout = input("Would you like to add a workout? ")
            
            if add_new_workout.title() == "No" :
                add_workout = False

            else :
                add_workout = True

            self.conn.commit()