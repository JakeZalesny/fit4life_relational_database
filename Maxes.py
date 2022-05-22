"""

"""
from sqlite3 import Connection
import Constants

class Maxes:
    def __init__(self, connection: Connection) -> None:
        self.maxes = {}
        self.modification = None
        self.conn = connection
        self.cur = self.conn.cursor()
        self.muscle_groups = Constants.DEFAULT_MUSCLE_GROUPS
    
    def create_maxes_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Maxes ([max_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
            [workout_name] TEXT, [max] INTEGER)""")
        self.conn.commit()
        

    def set_maxes(self):
        counter = 0
        workouts = Constants.MAXES
        self.cur.execute("SELECT workout_name FROM Maxes")
        existing_workouts = self.cur.fetchall()
        for i in range(len(existing_workouts) - 1):
            workouts.append(existing_workouts[i])

        
        for workout in range(len(workouts) - 1) :
            self.maxes[workout] = int(input(f"What is your max {workouts[workout]}? "))
            values = (workout ,self.maxes[workout])
            self.cur.execute("""INSERT INTO Maxes (workout_name, max) VALUES (?, ?)""", values)
            self.conn.commit()
            

    
    def get_all_maxes(self):
        return self.maxes
    
    def get_modification(self):
        for workout in Constants.MAXES:
            print(f"{workout}: {self.maxes[workout]}") 
        
        while self.modification not in self.maxes.keys():
            self.modification = input("Which max would you like to modify? ")    
            
            if self.modification in self.maxes.keys() :
                return self.modification
    
    def modify_max(self):
        modify_another = True
        while modify_another == True:
            self.maxes[self.modification] = int(input("What is your new max? "))
            values = (self.maxes[self.modification], self.modification)
            self.cur.execute("""UPDATE Maxes SET max = ? WHERE workout_name = ?""")
            self.conn.commit()
            modify_again = input("Would you like to modify another? (Yes/No)")
            if modify_again.title() == "No":
                modify_another = False
            
            else :
                modify_another = True