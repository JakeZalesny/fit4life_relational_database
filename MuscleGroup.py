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

    def add_workouts(self, muscle_group_list: list) -> None :
        add_workout = True
        while add_workout == True:
            muscle_group = input("What is the muscle group that you would like to add to? ") 
            workout = input("What is the workout you would like to add? ")
            
            if muscle_group.title() in muscle_group_list :
                values = (muscle_group, workout)
                self.cursor.execute("""SELECT * FROM ? """, values)
                workouts = self.cursor.fetchall()
                
                if workout.title() not in workouts :
                    self.cursor.execute("""INSERT INTO ? (workout_name) VALUES(?) """, values)
                
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
        
        self.connection.commit()
    
    def delete_workouts(self, muscle_group_list: list) -> None :
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


