######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

'''
     1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25

'''
for column in range(1,6):
    if column == 1:
        print("\t", end = ' ')
    print(column, end ='\t')
print()
print("\t ******************************* ")

for row in range(1,6):
    for column in range(1,6):
        if column ==1:
            print( f'{row} | \t', end =' ')
        print(f'{row * column}', end = '\t')
    print()


    
    