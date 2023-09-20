string = input("Input: ").split(' ')
s = []
for i in string:
    if i not in s:
        s.append(i)
print(s)

