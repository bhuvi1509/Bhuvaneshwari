mark=[]
tot=0
subjects=['Tamil','Engilsh','Maths','physics','chemistry','Computer science']
for i in range(6):
    m=int(input("Enter the mark = "))
    mark.append(m)
for i in range(6):
    tot = tot + int(mark[i])
avg = tot/5

if avg>=80 and avg<=100:
    print("Your Grade is A")
elif avg>=70 and avg<80:
    print("Your Grade is B")
elif avg>=60 and avg<70:
    print("Your Grade is C")
elif avg>=50 and avg<60:
    print("Your Grade is D")
elif avg>=45 and avg<50:
    print("Your Grade is E")
else:
    print("Wrong input")