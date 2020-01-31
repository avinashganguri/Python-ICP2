n = int(input("enter the value"))
list =[]
i=0
for i in range(n):
    x=int(input("enter weight in lbs:"))
    list.insert(i,x)
    list[i] = list[i]*0.45
print("weight of students in kgs", list)