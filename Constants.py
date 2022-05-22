"""
CONSTANTS
"""
DAYS_OF_WEEK = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DEFAULT_MUSCLE_GROUPS = ["Shoulders", "Chest", "Back", "Biceps", "Triceps", "Legs", "Abs"]
MAXES = ["Shoulder Press", "Bench Press", "Deadlift", "Hammer Curl (10 reps)", "Squat"]
DATABASE_FILE = "fit4Life.db"
DEFAULT_WORKOUTS = {
    "Shoulders":["Seated Dumbell Press", "Arnolds", "Standing Dumbell Flies", "Face Pulls", "EZ bar High Pull",
                "Seated Barbell Press", "Machine Shoulder Press", "Bent Over Reverse Fly", "Dumbell Incline Row",
                "Barbell Overhead Press", "Single Arm Front Cable Raise"],
    
    "Chest":["Bench Press", "Lower Incline Flies", "Incline Dumbell Press", "Incline Barbell Press", "Fly Machine",
            "Chest-Dips", "Cross-Over Flies","Elbows In Incline Push-Ups", "Cable Crossover", "Incline Flies", "Decline Dumbell Press"],

    "Back":[ "Deadlift", "Overhand Pull-Up", "Bent-Over Barbell Row", "Landmine Row", "Single-Arm Row", "Lat Pulldown (Wide Grip)", "Seated Cable Row (Close Grip)",
            "Cable/Dumbell Shrug", "Seated Cable Row (Wide Grip)", "Lat Pulldown (Close Grip)", "Chest Supported Row"],

    "Biceps":["Standing Curls", "Jailhouse Curls/Concentration Curls", "Preacher Curls", "Seated Wide Grip Curls", "Close-Grip Underhand Pull-Ups",
            "Hammer Curls", "Static Hold Curls", "Incline Dumbell Curl", "Reverse Grip Bent-Over Row", "Barbell Curl", "Facing-Away Cable Curl"],

    "Triceps":["Close Grip Bench Press", "Cable push down", "Dips", "Dumbell Skull-Crushers", "EZ bar Skull-Crushers", "JM Press", 
                "Dumbell Bench Press", "Tricep Kickback", "Overhead Cable Extension", "Standing Dumbell Extension", 
                "EZ Bar Reverse Grip Bench Press"],

    "Legs":["Squats", "Box Squats", "Decline Squats", "Leg-Press Machine", "Saturday Nigh Rides/Hip Thrusters", "Donkey Squat Machine",
            "Bulgarian Squats", "Front Squat", "Weighted Lunges", "Goblet Squat", "Leg Curl Machine"],

    "Abs":["Crunches", "Star Crunches", "Knees up Toe Touches", "Toe Touch V-Ups", "Crunch Machine", "Hanging Knee to Chests", 
            "Crucifix Crunches/Bear-Hugs", "Triangle Leg Raises", "Medicine Ball Russian Twist", "Beast Slams"],
}