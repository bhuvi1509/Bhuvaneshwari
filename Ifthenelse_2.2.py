'''2. We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. If the student's avg is, 94%, the student is eligible
 for admission in College 1 and College 2.'''

sub = int(input("Enter the number of subjects :"))
sum = 0
for i in range(sub):
    mark = int(input("Enter the mark of the subject :"))
    sum = sum + mark
    average = (sum / sub) 

print("Total mark is", sum)
print("Average of the total mark is ", average)
if average >= 93:
    print("You are eligible to get admission in College - 1")
elif average >= 89:
    print("You are eligible to get admission in College - 2 ")
elif average >= 97:
    print("You are  eligible to get admission in College - 3")
elif average >= 94:
    print("You are eligible to get admission in College - 1 and college - 2")
else:
    print("You are not eligible to get admission in those Colleges")