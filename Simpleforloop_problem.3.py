######## Problem 3  ###############
#Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ 


n = eval(input("Enter diamond's row: "))

for x in range(n):
    print(" " * (n- x), "#" * (2*x + 1))
for x in range(n - 2, -1, -1):
    print(" " * (n - x), "#" * (2*x + 1))