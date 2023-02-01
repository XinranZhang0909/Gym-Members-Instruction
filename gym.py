import math

# First Task
# Workout categories based on member's sex, age, and goals

fat_loss = "Gym workout for fat loss\n\nPlate thrusters (15 reps x 3 sets)\n\
Mountain climbers (20 reps x 3 sets)\nBox jumps (10 reps x 3 sets)\n\
Lunges (10 reps x 3 sets)\nRenegade rows (10 reps x 3 sets)\n\
Press ups (15 reps x 3 sets)\nTreadmill (10 mins x 3 sets)\n\
Supermans (10 reps x 3 sets)\nCrunches (10 reps x 3 sets)"

stretch_and_relax = "Gym workout for stretch and relax\n\nQuad stretchs (2 mins x 3 sets)\n\
Hamstring stretchs (2 mins x 3 sets)\nChest and shoulder stretchs (2 mins x 2 sets)\n\
Upper back stretchs (3 mins x 2 sets)\nBiceps stretchs (2 mins x 2 sets)\n\
Triceps stretchs (2 mins x 3 sets)\nHip flexors (2 mins x 3 sets)\n\
Calf stretchs (2 mins x 3 sets)\nLower back stretchs (2 mins x 3 sets)"

high_intensity_exercises = "Gym workout for high-intensity exercises\n\n\
Jumping jacks (20 reps x 4 sets)\nSprints (20 reps x 3 sets)\n\
Mountain climbers (20 reps x 4 sets)\nSquat jumps (20 reps x 4 sets)\n\
Lunges (20 reps x 3 sets)\nCrunches (20 reps x 3 sets)\n\
Treadmill (15 mins x 2 sets)\nSide planks (15 reps x 3 sets)\n\
Burpees (15 reps x 3 sets)"

strong_legs = "Gym workout for strong legs\n\nBack squats (10 reps x 5 sets)\n\
Hip thrusts (12 reps x 3 sets)\nOverhead presses (10 reps x 5 sets)\n\
Rack pulls (10 reps x 5 sets)\nSquats (10 reps x 4 sets)\n\
Dumbbell lunges (10 reps x 3 sets)\nLeg curls (15 reps x 3 sets)\n\
Standing calf raises (20 reps x 2 sets)"

strong_ABS = "Gym workout for strong ABS\n\nCross crunchs (12 reps x 3 sets)\n\
Knee ups (15 reps x 5 sets)\nHip thrusts (15 reps x 3 sets)\n\
Mountain climbers (15 reps x 3 sets)\nVertical hip thrusts (12 reps x 3 sets)\n\
Bicycles (15 mins x 2 sets)\nFront planks (15 mins x 3 sets)\n\
Dragon flags (12 reps x 4 sets)\nReverse crunches (10 reps x 3 sets)"

strong_shoulder_and_arms = "Gym workout for strong shoulder and arms\n\n\
Bench presses (10 reps x 5 sets)\nTriceps dips (10 reps x 5 sets)\n\
Incline dumbbell presses (12 reps x 3 sets)\ndumbbell flyes (15 reps x 3 sets)\n\
Triceps extensions (15 reps x 3 sets)\nPull ups (10 reps x 5 sets)\n\
Treadmill (15 mins x 2 sets)\nBent over rows (10 reps x 5 sets)\n\
Chin ups (10 reps x 3 sets)"

male_younger_than_18 = "Gym workout for a male younger than 18 years old\n\n\
High knees (20 reps x 3 sets)\nSquats (10 reps x 3 sets)\n\
Calf raises (10 reps x 3 sets)\nScissor jumps (12 reps x 3 sets)\n\
Burpees (10 reps x 3 sets)\nTreadmill (10 mins x 2 sets)"

female_younger_than_18 = "Gym workout for a female younger than 18 years old\n\n\
Squats (10 reps x 3 sets)\nCrunches (10 reps x 2 sets)\n\
Jumping jacks (10 reps x 3 sets)\nPush ups (10 reps x 2 sets)\n\
Burpees (10 reps x 3 sets)\nTreadmill (10 mins x 2 sets)"

male_at_least_18 = "Gym workout for a male at least 18 years old\n\n\
Standing biceps curls (20 reps x 3 sets)\nSeated incline curls (18 reps x 3 sets)\n\
Seated dumbbell presses (12 reps x 3 sets)\nLeg presses (15 reps x 3 sets)\n\
Bench presses (10 reps x 4 sets)\nTricep kickbacks (15 reps x 3 sets)\n\
Hip thrusts (12 reps x 3 sets)\nSeated rows (10 reps x 4 sets)"

female_at_least_18 = "Gym workout for a female at least 18 years old\n\n\
Lateral raises (15 reps x 3 sets)\nReverse flyes (12 reps x 3 sets)\n\
Hip thrusts (12 reps x 3 sets)\nIncline dumbbell presses (15 reps x 3 sets)\n\
Squats (10 reps x 4 sets)\nDumbbell lunges (10 reps x 3 sets)\n\
Leg presses (12 reps x 3 sets)\nDumbbell presses (10 reps x 4 sets)"

# Second Task
# Ask members to answer questions about themselves to help the program decide what sort of exercises suit the member better

# Ask members about their name, only accept alphabetical characters from [a-z][A-Z] and spaces
name=input("Please enter your name: ")
while str.isalpha(name.replace(' ','')) == False:
    print("Error: Only accept alphabetical characters and spaces for name")
    name=input("\nPlease enter your name: ")

# Ask members about their age, only accept a number between [0-110]
age=int(input("\nPlease enter your age: "))
while age < 0 or age > 110:
    print("Error: The age is a number between 0 to 110")
    age=int(input("\nPlease enter your age: "))

# Ask members about their sex, only accept "male" or "female" (case sensitive)
sex=input("\nPlease enter your biological sex (female/male): ")
while (sex == "female" or sex == "male") == False:
    print("Error: Please enter valid input")
    sex=input("\nPlease enter your biological sex (female/male): ")

# Ask members about their goals for exercising, only accept an option between 1 to 6
goal=input("\nWhat do you want to get out of your training? \n\
    1. Your goal is losing weight\n\
    2. Your goal is to staying calm and relax\n\
    3. Your goal is increasing your heart rate\n\
    4. Your goal is having stronger legs\n\
    5. Your goal is having stronger ABS\n\
    6. Your goal is having stronger shoulders and arms\n\
Choose a number between 1 to 6: ")
while (goal=="1" or goal=="2" or goal=="3" or goal=="4" or goal=="5" or goal=="6") == False:
    print("Error - It can only be a number between 1 to 6")
    goal=input("\nWhat do you want to get out of your training? \n\
    1. Your goal is losing weight\n\
    2. Your goal is to staying calm and relax\n\
    3. Your goal is increasing your heart rate\n\
    4. Your goal is having stronger legs\n\
    5. Your goal is having stronger ABS\n\
    6. Your goal is having stronger shoulders and arms\n\
Choose a number between 1 to 6: ")

# Ask members about how many days per week they can exercise, only accept a number between 1 to 7
days_per_week=input("\nHow many days per week you can train: ")
while (days_per_week=="1" or days_per_week=="2" or days_per_week=="3" or days_per_week=="4" or days_per_week=="5" or days_per_week=="6" or days_per_week=="7") == False:
    print("Error: It can only be a number between 1 to 7")
    days_per_week=input("\nHow many days per week you can train: ")

# Fourth Task
# Lower the intensity of the workouts for older people by lowering the number of reps/mins for each exercise
# Round the number of reps/mins up to the nearest whole integer

# For ages betweem (60,65], lower the reps/mins by 1% for every year above 60 years old
if age>60 and age<=65:
    year_above=age-60
    
    fat_loss = f"Gym workout for fat loss\n\nPlate thrusters ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*(1-0.01*year_above))} reps x 3 sets)\nBox jumps ({math.ceil(10*(1-0.01*year_above))} reps x 3 sets)\n\
Lunges ({math.ceil(10*(1-0.01*year_above))} reps x 3 sets)\nRenegade rows ({math.ceil(10*(1-0.01*year_above))} reps x 3 sets)\n\
Press ups ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\nTreadmill ({math.ceil(10*(1-0.01*year_above))} mins x 3 sets)\n\
Supermans ({math.ceil(10*(1-0.01*year_above))} reps x 3 sets)\nCrunches ({math.ceil(10*(1-0.01*year_above))} reps x 3 sets)"
    
    stretch_and_relax = f"Gym workout for stretch and relax\n\nQuad stretchs ({math.ceil(2*(1-0.01*year_above))} mins x 3 sets)\n\
Hamstring stretchs ({math.ceil(2*(1-0.01*year_above))} mins x 3 sets)\nChest and shoulder stretchs ({math.ceil(2*(1-0.01*year_above))} mins x 2 sets)\n\
Upper back stretchs ({math.ceil(3*(1-0.01*year_above))} mins x 2 sets)\nBiceps stretchs ({math.ceil(2*(1-0.01*year_above))} mins x 2 sets)\n\
Triceps stretchs ({math.ceil(2*(1-0.01*year_above))} mins x 3 sets)\nHip flexors ({math.ceil(2*(1-0.01*year_above))} mins x 3 sets)\n\
Calf stretchs ({math.ceil(2*(1-0.01*year_above))} mins x 3 sets)\nLower back stretchs ({math.ceil(2*(1-0.01*year_above))} mins x 3 sets)"
    
    high_intensity_exercises = f"Gym workout for high-intensity exercises\n\n\
Jumping jacks ({math.ceil(20*(1-0.01*year_above))} reps x 4 sets)\nSprints ({math.ceil(20*(1-0.01*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*(1-0.01*year_above))} reps x 4 sets)\nSquat jumps ({math.ceil(20*(1-0.01*year_above))} reps x 4 sets)\n\
Lunges ({math.ceil(20*(1-0.01*year_above))} reps x 3 sets)\nCrunches ({math.ceil(20*(1-0.01*year_above))} reps x 3 sets)\n\
Treadmill ({math.ceil(15*(1-0.01*year_above))} mins x 2 sets)\nSide planks ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\n\
Burpees ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)"
    
    strong_legs = f"Gym workout for strong legs\n\nBack squats ({math.ceil(10*(1-0.01*year_above))} reps x 5 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.01*year_above))} reps x 3 sets)\nOverhead presses ({math.ceil(10*(1-0.01*year_above))} reps x 5 sets)\n\
Rack pulls ({math.ceil(10*(1-0.01*year_above))} reps x 5 sets)\nSquats ({math.ceil(10*(1-0.01*year_above))} reps x 4 sets)\n\
Dumbbell lunges ({math.ceil(10*(1-0.01*year_above))} reps x 3 sets)\nLeg curls ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\n\
Standing calf raises ({math.ceil(20*(1-0.01*year_above))} reps x 2 sets)"

    strong_ABS = f"Gym workout for strong ABS\n\nCross crunchs ({math.ceil(12*(1-0.01*year_above))} reps x 3 sets)\n\
Knee ups ({math.ceil(15*(1-0.01*year_above))} reps x 5 sets)\nHip thrusts ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\nVertical hip thrusts ({math.ceil(12*(1-0.01*year_above))} reps x 3 sets)\n\
Bicycles ({math.ceil(15*(1-0.01*year_above))} mins x 2 sets)\nFront planks ({math.ceil(15*(1-0.01*year_above))} mins x 3 sets)\n\
Dragon flags ({math.ceil(12*(1-0.01*year_above))} reps x 4 sets)\nReverse crunches ({math.ceil(10*(1-0.01*year_above))} reps x 3 sets)"

    strong_shoulder_and_arms = f"Gym workout for strong shoulder and arms\n\n\
Bench presses ({math.ceil(10*(1-0.01*year_above))} reps x 5 sets)\nTriceps dips ({math.ceil(10*(1-0.01*year_above))} reps x 5 sets)\n\
Incline dumbbell presses ({math.ceil(12*(1-0.01*year_above))} reps x 3 sets)\ndumbbell flyes ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\n\
Triceps extensions ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\nPull ups ({math.ceil(10*(1-0.01*year_above))} reps x 5 sets)\n\
Treadmill ({math.ceil(15*(1-0.01*year_above))} mins x 2 sets)\nBent over rows ({math.ceil(10*(1-0.01*year_above))} reps x 5 sets)\n\
Chin ups ({math.ceil(10*(1-0.01*year_above))} reps x 3 sets)"

    male_at_least_18 = f"Gym workout for a male at least 18 years old\n\n\
Standing biceps curls ({math.ceil(20*(1-0.01*year_above))} reps x 3 sets)\nSeated incline curls ({math.ceil(18*(1-0.01*year_above))} reps x 3 sets)\n\
Seated dumbbell presses ({math.ceil(12*(1-0.01*year_above))} reps x 3 sets)\nLeg presses ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\n\
Bench presses ({math.ceil(10*(1-0.01*year_above))} reps x 4 sets)\nTricep kickbacks ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.01*year_above))} reps x 3 sets)\nSeated rows ({math.ceil(10*(1-0.01*year_above))} reps x 4 sets)"

    female_at_least_18 = f"Gym workout for a female at least 18 years old\n\n\
Lateral raises ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\nReverse flyes ({math.ceil(12*(1-0.01*year_above))} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.01*year_above))} reps x 3 sets)\nIncline dumbbell presses ({math.ceil(15*(1-0.01*year_above))} reps x 3 sets)\n\
Squats ({math.ceil(10*(1-0.01*year_above))} reps x 4 sets)\nDumbbell lunges ({math.ceil(10*(1-0.01*year_above))} reps x 3 sets)\n\
Leg presses ({math.ceil(12*(1-0.01*year_above))} reps x 3 sets)\nDumbbell presses ({math.ceil(10*(1-0.01*year_above))} reps x 4 sets)"

# For ages between (65,75], lower the reps/mins by 5% plus 2% for every year above 65 years old
if age>65 and age<=75:
    year_above=age-65

    fat_loss = f"Gym workout for fat loss\n\nPlate thrusters ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*(1-0.05-0.02*year_above))} reps x 3 sets)\nBox jumps ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Lunges ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 3 sets)\nRenegade rows ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Press ups ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\nTreadmill ({math.ceil(10*(1-0.05-0.02*year_above))} mins x 3 sets)\n\
Supermans ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 3 sets)\nCrunches ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 3 sets)"
    
    stretch_and_relax = f"Gym workout for stretch and relax\n\nQuad stretchs ({math.ceil(2*(1-0.05-0.02*year_above))} mins x 3 sets)\n\
Hamstring stretchs ({math.ceil(2*(1-0.05-0.02*year_above))} mins x 3 sets)\nChest and shoulder stretchs ({math.ceil(2*(1-0.05-0.02*year_above))} mins x 2 sets)\n\
Upper back stretchs ({math.ceil(3*(1-0.05-0.02*year_above))} mins x 2 sets)\nBiceps stretchs ({math.ceil(2*(1-0.05-0.02*year_above))} mins x 2 sets)\n\
Triceps stretchs ({math.ceil(2*(1-0.05-0.02*year_above))} mins x 3 sets)\nHip flexors ({math.ceil(2*(1-0.05-0.02*year_above))} mins x 3 sets)\n\
Calf stretchs ({math.ceil(2*(1-0.05-0.02*year_above))} mins x 3 sets)\nLower back stretchs ({math.ceil(2*(1-0.05-0.02*year_above))} mins x 3 sets)"
    
    high_intensity_exercises = f"Gym workout for high-intensity exercises\n\n\
Jumping jacks ({math.ceil(20*(1-0.05-0.02*year_above))} reps x 4 sets)\nSprints ({math.ceil(20*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*(1-0.05-0.02*year_above))} reps x 4 sets)\nSquat jumps ({math.ceil(20*(1-0.05-0.02*year_above))} reps x 4 sets)\n\
Lunges ({math.ceil(20*(1-0.05-0.02*year_above))} reps x 3 sets)\nCrunches ({math.ceil(20*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Treadmill ({math.ceil(15*(1-0.05-0.02*year_above))} mins x 2 sets)\nSide planks ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Burpees ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)"
    
    strong_legs = f"Gym workout for strong legs\n\nBack squats ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 5 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 3 sets)\nOverhead presses ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 5 sets)\n\
Rack pulls ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 5 sets)\nSquats ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 4 sets)\n\
Dumbbell lunges ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 3 sets)\nLeg curls ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Standing calf raises ({math.ceil(20*(1-0.05-0.02*year_above))} reps x 2 sets)"

    strong_ABS = f"Gym workout for strong ABS\n\nCross crunchs ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Knee ups ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 5 sets)\nHip thrusts ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\nVertical hip thrusts ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Bicycles ({math.ceil(15*(1-0.05-0.02*year_above))} mins x 2 sets)\nFront planks ({math.ceil(15*(1-0.05-0.02*year_above))} mins x 3 sets)\n\
Dragon flags ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 4 sets)\nReverse crunches ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 3 sets)"

    strong_shoulder_and_arms = f"Gym workout for strong shoulder and arms\n\n\
Bench presses ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 5 sets)\nTriceps dips ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 5 sets)\n\
Incline dumbbell presses ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 3 sets)\ndumbbell flyes ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Triceps extensions ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\nPull ups ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 5 sets)\n\
Treadmill ({math.ceil(15*(1-0.05-0.02*year_above))} mins x 2 sets)\nBent over rows ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 5 sets)\n\
Chin ups ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 3 sets)"

    male_at_least_18 = f"Gym workout for a male at least 18 years old\n\n\
Standing biceps curls ({math.ceil(20*(1-0.05-0.02*year_above))} reps x 3 sets)\nSeated incline curls ({math.ceil(18*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Seated dumbbell presses ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 3 sets)\nLeg presses ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Bench presses ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 4 sets)\nTricep kickbacks ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 3 sets)\nSeated rows ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 4 sets)"

    female_at_least_18 = f"Gym workout for a female at least 18 years old\n\n\
Lateral raises ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\nReverse flyes ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 3 sets)\nIncline dumbbell presses ({math.ceil(15*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Squats ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 4 sets)\nDumbbell lunges ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 3 sets)\n\
Leg presses ({math.ceil(12*(1-0.05-0.02*year_above))} reps x 3 sets)\nDumbbell presses ({math.ceil(10*(1-0.05-0.02*year_above))} reps x 4 sets)"

# For ages between (75,80], lower the reps/mins by 25% plus 3% for every year above 75 years old
if age>75 and age<=80:
    year_above=age-75

    fat_loss = f"Gym workout for fat loss\n\nPlate thrusters ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*(1-0.25-0.03*year_above))} reps x 3 sets)\nBox jumps ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Lunges ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 3 sets)\nRenegade rows ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Press ups ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\nTreadmill ({math.ceil(10*(1-0.25-0.03*year_above))} mins x 3 sets)\n\
Supermans ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 3 sets)\nCrunches ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 3 sets)"
    
    stretch_and_relax = f"Gym workout for stretch and relax\n\nQuad stretchs ({math.ceil(2*(1-0.25-0.03*year_above))} mins x 3 sets)\n\
Hamstring stretchs ({math.ceil(2*(1-0.25-0.03*year_above))} mins x 3 sets)\nChest and shoulder stretchs ({math.ceil(2*(1-0.25-0.03*year_above))} mins x 2 sets)\n\
Upper back stretchs ({math.ceil(3*(1-0.25-0.03*year_above))} mins x 2 sets)\nBiceps stretchs ({math.ceil(2*(1-0.25-0.03*year_above))} mins x 2 sets)\n\
Triceps stretchs ({math.ceil(2*(1-0.25-0.03*year_above))} mins x 3 sets)\nHip flexors ({math.ceil(2*(1-0.25-0.03*year_above))} mins x 3 sets)\n\
Calf stretchs ({math.ceil(2*(1-0.25-0.03*year_above))} mins x 3 sets)\nLower back stretchs ({math.ceil(2*(1-0.25-0.03*year_above))} mins x 3 sets)"
    
    high_intensity_exercises = f"Gym workout for high-intensity exercises\n\n\
Jumping jacks ({math.ceil(20*(1-0.25-0.03*year_above))} reps x 4 sets)\nSprints ({math.ceil(20*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*(1-0.25-0.03*year_above))} reps x 4 sets)\nSquat jumps ({math.ceil(20*(1-0.25-0.03*year_above))} reps x 4 sets)\n\
Lunges ({math.ceil(20*(1-0.25-0.03*year_above))} reps x 3 sets)\nCrunches ({math.ceil(20*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Treadmill ({math.ceil(15*(1-0.25-0.03*year_above))} mins x 2 sets)\nSide planks ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Burpees ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)"
    
    strong_legs = f"Gym workout for strong legs\n\nBack squats ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 5 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 3 sets)\nOverhead presses ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 5 sets)\n\
Rack pulls ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 5 sets)\nSquats ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 4 sets)\n\
Dumbbell lunges ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 3 sets)\nLeg curls ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Standing calf raises ({math.ceil(20*(1-0.25-0.03*year_above))} reps x 2 sets)"

    strong_ABS = f"Gym workout for strong ABS\n\nCross crunchs ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Knee ups ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 5 sets)\nHip thrusts ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\nVertical hip thrusts ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Bicycles ({math.ceil(15*(1-0.25-0.03*year_above))} mins x 2 sets)\nFront planks ({math.ceil(15*(1-0.25-0.03*year_above))} mins x 3 sets)\n\
Dragon flags ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 4 sets)\nReverse crunches ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 3 sets)"

    strong_shoulder_and_arms = f"Gym workout for strong shoulder and arms\n\n\
Bench presses ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 5 sets)\nTriceps dips ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 5 sets)\n\
Incline dumbbell presses ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 3 sets)\ndumbbell flyes ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Triceps extensions ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\nPull ups ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 5 sets)\n\
Treadmill ({math.ceil(15*(1-0.25-0.03*year_above))} mins x 2 sets)\nBent over rows ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 5 sets)\n\
Chin ups ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 3 sets)"

    male_at_least_18 = f"Gym workout for a male at least 18 years old\n\n\
Standing biceps curls ({math.ceil(20*(1-0.25-0.03*year_above))} reps x 3 sets)\nSeated incline curls ({math.ceil(18*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Seated dumbbell presses ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 3 sets)\nLeg presses ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Bench presses ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 4 sets)\nTricep kickbacks ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 3 sets)\nSeated rows ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 4 sets)"

    female_at_least_18 = f"Gym workout for a female at least 18 years old\n\n\
Lateral raises ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\nReverse flyes ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 3 sets)\nIncline dumbbell presses ({math.ceil(15*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Squats ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 4 sets)\nDumbbell lunges ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 3 sets)\n\
Leg presses ({math.ceil(12*(1-0.25-0.03*year_above))} reps x 3 sets)\nDumbbell presses ({math.ceil(10*(1-0.25-0.03*year_above))} reps x 4 sets)"

# For ages between (80,90], lower the reps/mins by 40% plus 4% for every year above 80 years old
if age>80 and age<=90:
    year_above=age-80

    fat_loss = f"Gym workout for fat loss\n\nPlate thrusters ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*(1-0.4-0.04*year_above))} reps x 3 sets)\nBox jumps ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Lunges ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 3 sets)\nRenegade rows ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Press ups ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\nTreadmill ({math.ceil(10*(1-0.4-0.04*year_above))} mins x 3 sets)\n\
Supermans ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 3 sets)\nCrunches ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 3 sets)"
    
    stretch_and_relax = f"Gym workout for stretch and relax\n\nQuad stretchs ({math.ceil(2*(1-0.4-0.04*year_above))} mins x 3 sets)\n\
Hamstring stretchs ({math.ceil(2*(1-0.4-0.04*year_above))} mins x 3 sets)\nChest and shoulder stretchs ({math.ceil(2*(1-0.4-0.04*year_above))} mins x 2 sets)\n\
Upper back stretchs ({math.ceil(3*(1-0.4-0.04*year_above))} mins x 2 sets)\nBiceps stretchs ({math.ceil(2*(1-0.4-0.04*year_above))} mins x 2 sets)\n\
Triceps stretchs ({math.ceil(2*(1-0.4-0.04*year_above))} mins x 3 sets)\nHip flexors ({math.ceil(2*(1-0.4-0.04*year_above))} mins x 3 sets)\n\
Calf stretchs ({math.ceil(2*(1-0.4-0.04*year_above))} mins x 3 sets)\nLower back stretchs ({math.ceil(2*(1-0.4-0.04*year_above))} mins x 3 sets)"
    
    high_intensity_exercises = f"Gym workout for high-intensity exercises\n\n\
Jumping jacks ({math.ceil(20*(1-0.4-0.04*year_above))} reps x 4 sets)\nSprints ({math.ceil(20*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*(1-0.4-0.04*year_above))} reps x 4 sets)\nSquat jumps ({math.ceil(20*(1-0.4-0.04*year_above))} reps x 4 sets)\n\
Lunges ({math.ceil(20*(1-0.4-0.04*year_above))} reps x 3 sets)\nCrunches ({math.ceil(20*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Treadmill ({math.ceil(15*(1-0.4-0.04*year_above))} mins x 2 sets)\nSide planks ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Burpees ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)"
    
    strong_legs = f"Gym workout for strong legs\n\nBack squats ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 5 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 3 sets)\nOverhead presses ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 5 sets)\n\
Rack pulls ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 5 sets)\nSquats ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 4 sets)\n\
Dumbbell lunges ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 3 sets)\nLeg curls ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Standing calf raises ({math.ceil(20*(1-0.4-0.04*year_above))} reps x 2 sets)"

    strong_ABS = f"Gym workout for strong ABS\n\nCross crunchs ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Knee ups ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 5 sets)\nHip thrusts ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Mountain climbers ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\nVertical hip thrusts ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Bicycles ({math.ceil(15*(1-0.4-0.04*year_above))} mins x 2 sets)\nFront planks ({math.ceil(15*(1-0.4-0.04*year_above))} mins x 3 sets)\n\
Dragon flags ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 4 sets)\nReverse crunches ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 3 sets)"

    strong_shoulder_and_arms = f"Gym workout for strong shoulder and arms\n\n\
Bench presses ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 5 sets)\nTriceps dips ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 5 sets)\n\
Incline dumbbell presses ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 3 sets)\ndumbbell flyes ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Triceps extensions ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\nPull ups ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 5 sets)\n\
Treadmill ({math.ceil(15*(1-0.4-0.04*year_above))} mins x 2 sets)\nBent over rows ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 5 sets)\n\
Chin ups ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 3 sets)"

    male_at_least_18 = f"Gym workout for a male at least 18 years old\n\n\
Standing biceps curls ({math.ceil(20*(1-0.4-0.04*year_above))} reps x 3 sets)\nSeated incline curls ({math.ceil(18*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Seated dumbbell presses ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 3 sets)\nLeg presses ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Bench presses ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 4 sets)\nTricep kickbacks ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 3 sets)\nSeated rows ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 4 sets)"

    female_at_least_18 = f"Gym workout for a female at least 18 years old\n\n\
Lateral raises ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\nReverse flyes ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 3 sets)\nIncline dumbbell presses ({math.ceil(15*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Squats ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 4 sets)\nDumbbell lunges ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 3 sets)\n\
Leg presses ({math.ceil(12*(1-0.4-0.04*year_above))} reps x 3 sets)\nDumbbell presses ({math.ceil(10*(1-0.4-0.04*year_above))} reps x 4 sets)"

# For ages between (90,110], lower the reps/mins by 80%
if age>90 and age<=110:
    fat_loss = f"Gym workout for fat loss\n\nPlate thrusters ({math.ceil(15*0.2)} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*0.2)} reps x 3 sets)\nBox jumps ({math.ceil(10*0.2)} reps x 3 sets)\n\
Lunges ({math.ceil(10*0.2)} reps x 3 sets)\nRenegade rows ({math.ceil(10*0.2)} reps x 3 sets)\n\
Press ups ({math.ceil(15*0.2)} reps x 3 sets)\nTreadmill ({math.ceil(10*0.2)} mins x 3 sets)\n\
Supermans ({math.ceil(10*0.2)} reps x 3 sets)\nCrunches ({math.ceil(10*0.2)} reps x 3 sets)"
    
    stretch_and_relax = f"Gym workout for stretch and relax\n\nQuad stretchs ({math.ceil(2*0.2)} mins x 3 sets)\n\
Hamstring stretchs ({math.ceil(2*0.2)} mins x 3 sets)\nChest and shoulder stretchs ({math.ceil(2*0.2)} mins x 2 sets)\n\
Upper back stretchs ({math.ceil(3*0.2)} mins x 2 sets)\nBiceps stretchs ({math.ceil(2*0.2)} mins x 2 sets)\n\
Triceps stretchs ({math.ceil(2*0.2)} mins x 3 sets)\nHip flexors ({math.ceil(2*0.2)} mins x 3 sets)\n\
Calf stretchs ({math.ceil(2*0.2)} mins x 3 sets)\nLower back stretchs ({math.ceil(2*0.2)} mins x 3 sets)"
    
    high_intensity_exercises = f"Gym workout for high-intensity exercises\n\n\
Jumping jacks ({math.ceil(20*0.2)} reps x 4 sets)\nSprints ({math.ceil(20*0.2)} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*0.2)} reps x 4 sets)\nSquat jumps ({math.ceil(20*0.2)} reps x 4 sets)\n\
Lunges ({math.ceil(20*0.2)} reps x 3 sets)\nCrunches ({math.ceil(20*0.2)} reps x 3 sets)\n\
Treadmill ({math.ceil(15*0.2)} mins x 2 sets)\nSide planks ({math.ceil(15*0.2)} reps x 3 sets)\n\
Burpees ({math.ceil(15*0.2)} reps x 3 sets)"
    
    strong_legs = f"Gym workout for strong legs\n\nBack squats ({math.ceil(10*0.2)} reps x 5 sets)\n\
Hip thrusts ({math.ceil(12*0.2)} reps x 3 sets)\nOverhead presses ({math.ceil(10*0.2)} reps x 5 sets)\n\
Rack pulls ({math.ceil(10*0.2)} reps x 5 sets)\nSquats ({math.ceil(10*0.2)} reps x 4 sets)\n\
Dumbbell lunges ({math.ceil(10*0.2)} reps x 3 sets)\nLeg curls ({math.ceil(15*0.2)} reps x 3 sets)\n\
Standing calf raises ({math.ceil(20*0.2)} reps x 2 sets)"

    strong_ABS = f"Gym workout for strong ABS\n\nCross crunchs ({math.ceil(12*0.2)} reps x 3 sets)\n\
Knee ups ({math.ceil(15*0.2)} reps x 5 sets)\nHip thrusts ({math.ceil(15*0.2)} reps x 3 sets)\n\
Mountain climbers ({math.ceil(15*0.2)} reps x 3 sets)\nVertical hip thrusts ({math.ceil(12*0.2)} reps x 3 sets)\n\
Bicycles ({math.ceil(15*0.2)} mins x 2 sets)\nFront planks ({math.ceil(15*0.2)} mins x 3 sets)\n\
Dragon flags ({math.ceil(12*0.2)} reps x 4 sets)\nReverse crunches ({math.ceil(10*0.2)} reps x 3 sets)"

    strong_shoulder_and_arms = f"Gym workout for strong shoulder and arms\n\n\
Bench presses ({math.ceil(10*0.2)} reps x 5 sets)\nTriceps dips ({math.ceil(10*0.2)} reps x 5 sets)\n\
Incline dumbbell presses ({math.ceil(12*0.2)} reps x 3 sets)\ndumbbell flyes ({math.ceil(15*0.2)} reps x 3 sets)\n\
Triceps extensions ({math.ceil(15*0.2)} reps x 3 sets)\nPull ups ({math.ceil(10*0.2)} reps x 5 sets)\n\
Treadmill ({math.ceil(15*0.2)} mins x 2 sets)\nBent over rows ({math.ceil(10*0.2)} reps x 5 sets)\n\
Chin ups ({math.ceil(10*0.2)} reps x 3 sets)"

    male_at_least_18 = f"Gym workout for a male at least 18 years old\n\n\
Standing biceps curls ({math.ceil(20*0.2)} reps x 3 sets)\nSeated incline curls ({math.ceil(18*0.2)} reps x 3 sets)\n\
Seated dumbbell presses ({math.ceil(12*0.2)} reps x 3 sets)\nLeg presses ({math.ceil(15*0.2)} reps x 3 sets)\n\
Bench presses ({math.ceil(10*0.2)} reps x 4 sets)\nTricep kickbacks ({math.ceil(15*0.2)} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*0.2)} reps x 3 sets)\nSeated rows ({math.ceil(10*0.2)} reps x 4 sets)"

    female_at_least_18 = f"Gym workout for a female at least 18 years old\n\n\
Lateral raises ({math.ceil(15*0.2)} reps x 3 sets)\nReverse flyes ({math.ceil(12*0.2)} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*0.2)} reps x 3 sets)\nIncline dumbbell presses ({math.ceil(15*0.2)} reps x 3 sets)\n\
Squats ({math.ceil(10*0.2)} reps x 4 sets)\nDumbbell lunges ({math.ceil(10*0.2)} reps x 3 sets)\n\
Leg presses ({math.ceil(12*0.2)} reps x 3 sets)\nDumbbell presses ({math.ceil(10*0.2)} reps x 4 sets)"

# Third Task
# Decide what exercise suits each member based on their input

print(f"\nHello {name}! Here is your training:\n\
-------------------------------------------------------------------------------------")

workout_goal=[fat_loss,stretch_and_relax,high_intensity_exercises,strong_legs,strong_ABS,strong_shoulder_and_arms,male_younger_than_18,female_younger_than_18,male_at_least_18,female_at_least_18]

# The first workout is from category [1-6], depending on their goals
first_workout=workout_goal[int(goal)-1]

# The second workout is from categories [7-10], depending on their sex and age
if sex == "female":
    if age < 18:
        second_workout=workout_goal[7]
    else:
        second_workout=workout_goal[9]
else:
    if age < 18:
        second_workout=workout_goal[6]
    else:
        second_workout=workout_goal[8]

# Depending on how many days per week they want to train, repeat them for the rest of the week
i=1
while i <= int(days_per_week):
    if i%2 == 1:
        print(f"Day {i}\n{first_workout}\n-------------------------------------------------------------------------------------")
    else:
        print(f"Day {i}\n{second_workout}\n-------------------------------------------------------------------------------------")
    i += 1

# End of Program
print(f"\nBye {name}.")
