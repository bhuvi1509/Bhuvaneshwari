'''Write code for the following program
1. Calcualte and print users age - Write a program to ask the user for his/her name and print 'Hello', user's name. 
Ask what year they were born.  get the year from the user. Print 'You are <age> years old'.'''

name=(input("Enter your name: "))
print("Hello", name)
birth_year = int(input("Enter your year of birth: "))
current_year = int(input("Enter the current year: "))
age =  current_year - birth_year 
print("Hai", name,", Your age is :", age)
