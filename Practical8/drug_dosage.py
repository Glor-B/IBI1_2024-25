rec_dose = 15
weight = float(input('Please enter children weight (kg)):'))
strength = int(input("Please choose strength of paracetamol: 120 / 250 (mg/5ml):"))

def calculator(weight, strength):
    if not 10 <= weight <= 100:
        return 'Wrong children weight'
    if strength == 120 or strength == 250:
        volume = 15 * weight / strength
        return volume
    else:
        return 'Wrong paracetamol strength'
    

print('Recommended dose:', calculator(weight, strength))