# store one's weight and height
# a: weight; b: height
a = 60
b = 1.70
# calculate one's bmi
bmi = a / b ** 2
# judge the bmi range
if bmi <= 18.5:
    # print the result
    print("Your BMI is", bmi, "You are underweight! Please eat more :(")
elif bmi >= 30:
    print("Your BMI is", bmi, "Sorry, you are obese! Wanna some exercise?")
else:
    print("Your BMI is", bmi,". Wow！You are in normal weight!")