#write code for both for and while loop
#Get marks from 5  students and calculate avg

#for loop:

'''total =0
for i in range(5):
    mark = int(input("Enter the mark: "))
    total += mark
    avg = total / 5
print("Average is", avg)'''

#while loop:


total = 0
noOfStudents = 5
i = 0
while (i < noOfStudents):
     mark = int(input("Enter the mark: "))
     total += mark
     avg = total / noOfStudents
     i += 1
print ("Avg is ",  avg)
