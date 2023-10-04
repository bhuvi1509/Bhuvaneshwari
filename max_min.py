''' 4. Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or mininum.
Find the answer and print.'''

num = int(input("Enter the number of inputs:" ))
for i in range(num):
    numbers = int(input("Enthe the number: "))
find = input("What we want to find mininmum or maximum of the numbers: ")
maximum = max(numbers)
minimum = min(numbers)
#find = input("What we want to find mininmum or maximum of the numbers: ")
if find == numbers:
    print("Maximum of three numbers is ", maximum)
else:
    print("Minimum of three numbers is",minimum)