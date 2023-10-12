'''
1       5 6 7
1 2     5 6 7
1   3   5 6 7
1     4 5 6 7
1       5 6 7 8 9 0 1
'''
'''for row in range(5):
    for column in range(11):
        if column == 0 or column == 4 or column == 5 or row == column or column == 6:
            print('*', end = ' ')
            if row == 4 or column == 10:
                print('*', end =' ')
        else:
            print(' ', end = ' ')
    print() '''

'''
1       5  6  7       1
1 2     5  6  7       1
1   3   5  6  7       1
1     4 5  6  7       1
1       5  6  7 8 9 0 1

'''

for row in range(5):
    for column in range(11):
        if column == 0 or row == column or column == 4 or column == 5 or column == 6 or column ==10:            
             print('*', end = ' ')
             if row == 4 or row == 5- 1  :
                print('*', end =' ')
        else:
            print(' ', end = ' ')
    print()
    


