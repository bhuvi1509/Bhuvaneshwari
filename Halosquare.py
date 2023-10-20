'''
1 2 3 4 5 
1       5
1       5
1       5
1 2 3 4 5
'''


        

for row in range(5):
    for column in range(5):
        if row == 0 or row == 4 or column == 0 or column == 4:
            print('*', end = ' ')
        else:
            print(' ',end= ' ')
    print()
