fruit=['apple', 'mango', 'banana', 'mango','apple']
unique_fruit=[]
for a in fruit:
    if a not in unique_fruit:
        unique_fruit.append(a)
print(unique_fruit)