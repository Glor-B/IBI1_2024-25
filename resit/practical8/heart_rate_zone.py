def calculator(age, heart_rate):
    max = 220 - age
    percentage = heart_rate / max
    if 0.5 < percentage <= 0.6:
        print("Zone 1 (Very light exercise)")
    elif 0.6 < percentage <=0.7:
        print("Zone 2 (Light exercise)")
    elif 0.7 < percentage <= 0.8:
        print("Zone 3 (Moderate exercise)")
    elif 0.8 < percentage <= 0.9:
        print("Zone 4 (Hard exercise)")
    elif 0.9 < percentage <= 1:
        print("Zone 5 (Maximum)")

age= int(input("Enter your age:"))
heart_rate = int(input("Enter your current heart rate:"))
calculator(age, heart_rate)