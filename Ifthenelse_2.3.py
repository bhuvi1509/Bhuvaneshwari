'''3. ############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input. The chart below shows the range.
http://www.milkaclarkestrokefoundation.org/uploads/2/4/5/9/2459046/bmi-index_orig.jpg
Use logical and/or conditions.
'''


'''

Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more 

'''

weight = int(input("Enter your weight : "))
height = float(input("Enter your height : "))
bmi = weight / (height)**2

if bmi < 18.5:
    print("You are Underweight", bmi)
elif  bmi>=18.5 and bmi<25:
    print(" you are Normal", bmi)
elif bmi >= 25 and bmi < 30:
   print(" You are Overweight", bmi)
else:
   print("Obesity")