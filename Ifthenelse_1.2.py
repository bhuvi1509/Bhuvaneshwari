########## Problem 2 ##########
##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

#find how many choc and cake the user can buy.

print("Welcome to the shop")
iteam =input(" iteams you want :")
choc = 1
cake =1
choc_and_cake =2 
budget = int(input("What is your budget amount:"))
if iteam == choc:
    choc = int(input("Enter how many choc:"))
    total = choc * 200
    print("Total amount of choc is", total)
elif iteam == cake:
    cake = int(input("Enter how many cake you want:"))
    total = cake *150
    print("total amount of cake is", total)
else:
    choc_and_cake = int(input("Enter how many choc and cake you want:"))
    total = (choc * 200) + (cake * 150)
    print("total amount of choc and cake is", total)
