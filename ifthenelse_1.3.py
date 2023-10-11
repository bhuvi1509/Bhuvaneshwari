############## Problem 3 ##############
#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

sub =int(input("Enter the number of subject:"))
for i in range(sub):
    mark = int(input("Enter the mark:"))
if mark ==100:
    print("Your grade is A")
elif mark<=90:
    print("Your grade is B")
elif mark <=60:
    print("Your grade is C")
elif mark<=50:
    print("Your grade is D")
elif mark>=50:
    print("Your grade is F")
else:
    print("Your grade is D")