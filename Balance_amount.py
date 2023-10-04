'''2. The user just bought a few things in your  shop. Ask the user what he bought. 
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user. 
Hint - use float datatype'''

print("Welcome to our shop")
things =int (input("What are the thing you bought:"))
sum = 0
for i in range(things):
    items = input("Enter the things name: ")
    amount = float(input("Enter the amount of the item:"))
    print(items, amount)
    sum=sum+amount
print("The total amount is ",sum)
money = float(input("Pay your bill amount:"))
balance = money - sum
print("Here your change",balance)
print("Thanks for coming")


