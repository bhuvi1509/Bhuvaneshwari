
######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.



def print_table(n, i=1):
 
    if (i == 13):  
        return
    print(n, "*", i, "=", n * i)
    i += 1  
    print_table(n, i)
 
n = int(input("Enter the table number: "))
print_table(n)
 