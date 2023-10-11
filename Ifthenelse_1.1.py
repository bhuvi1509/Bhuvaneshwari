############ Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.

'''AMOUNT                             INCOME TAX RATE
Up to ₹2,50,000                     0%
₹2,50,001  – ₹5,00,000               5% above ₹2,50,000
₹5,00,001  – ₹7,50,000               10% above ₹5,00,000 + ₹12,500
₹7,50,001  – ₹10,00,000              15% above ₹7,50,000 + ₹37,500
₹10,00,001 – ₹12,50,000             20% above ₹10,00,000 + ₹75,000
₹12,50,001 – ₹15,00,000             25% above ₹12,50,000 + ₹1,25,000
Above ₹15,00,001                    30% above ₹15,00,000 + ₹1,87,500'''

print(".....Welcome to Income tax calculation.....")
salary = int(input("Enter your salary amount:"))
if salary <= 250000:  
    tax = 0

elif salary <= 500000:
    tax = (salary- 250000) * 0.05

elif salary <= 750000: 
    tax = (salary - 500000) * 0.10 + 12500 

elif salary <= 1000000: 
    tax = (salary - 750000) * 0.15 + 37500 

elif salary <= 1250000:
    tax = (salary - 1000000) * 0.20 + 75000 

elif salary <= 1500000: 
    tax = (salary - 1250000) * 0.25 + 125000 

else:
    tax = (salary- 1500000) * 0.30 + 187500
print("Your tax amount is", tax)

if tax > 0:
    amount = int(input("Pay your tax amount:"))
    balance = amount - tax
    if amount==tax:
        print("You pay the full amount")
    
    elif amount > tax:
        print("you are not pay the full amount, pay the balance",balance)
        

    elif amount < tax:
        print("Your pay more amount here your balance", balance)

    else:
        print("You want to not pay a amount extra")
print("Thank you......")
