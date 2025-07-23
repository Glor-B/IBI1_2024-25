class patient_modelling:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = float(height)
        self.weight = float(weight)
    def BMI_calculator(self):
        BMI = round(self.weight / self.height ** 2, 2)
        if BMI <= 18.5:
            # print the result
            print("Your BMI is", BMI, ".You are underweight.")
        elif BMI >= 30:
            print("Your BMI is", BMI, ".You are obese.")
        else:
            print("Your BMI is", BMI, ". You are in normal weight.")


name, age, height, weight = input('Enter patient name:'), input('Enter patient age:'), input('Enter height (meter):'), input('Enter weight (kg):')
patient_modelling(name, age, height, weight).BMI_calculator()