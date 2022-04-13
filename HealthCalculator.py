#Rowan Patton
#HealthCalculator.py
#7/29/2021

#program to calculate the BMI
#based on user's input for height and wight
#program calculates max heart rate at varying degrees of exercise intensity
#based on age and resting heart rate input by user

print('Please enter the following values for the user:\n')

#have user input information for caluclations. if they are not numeric, continue to ask until they are
height_in = input('Height in inches: ')
while height_in.isnumeric() == False:
        height_in = input("That's not a valid response. Enter height in inches: ")
height_in = float(height_in)   

weight_lb = input('Weight in pounds: ')
while weight_lb.isnumeric() == False:
        weight_lb = input("That's not a valid response. Enter weight in pounds: ")
weight_lb = float(weight_lb)

age = input('Current age: ')
while age.isnumeric() == False:
        age = input("That's not a valid response. Enter current age: ")
age = float(age)

heart_rate = input('Resting heart rate: ')
while heart_rate.isnumeric() == False:
        heart_rate = input("That's not a valid response. Enter resting heart rate: ")
heart_rate = float(heart_rate)

#convert weight to kilogtams and height to m^2. round the answer to 2 decimal points
weight_kg = weight_lb * .453592
height_m = height_in * .0254
height_m2 = height_m * height_m
bmi = round(weight_kg / height_m2, 2)

#based on bmi calculation, determine bmi category
if bmi < 18.5:
    body_score = 'Underweight'
elif bmi < 25:
    body_score = 'Normal weight'
elif bmi < 30:
    body_score = 'Overweight'
else:
    body_score = 'Obese'
print()
print('*' * 10, 'Results', '*' *10)
print('Your BMI is: ', str(bmi), ' -- ', body_score)
print()
print()
print('*' * 10, 'Exercise Intensity Heart Rates', '*' *10)
print()
print('Intensity\t Max Heart Rate')

#create a loop to print numbers 50-95 in increments of 5.
#calculate the max heart rate based on the intensity percentage (changed to decimal) listed
for i in range(50, 100,5):
    max_heart_rate = int((((220-age)-heart_rate)* (i/100))+heart_rate)
    print(str(i)+'%\t\t\t'+ str(max_heart_rate))
    
    
