marks = [
[78, 76, 94, 86, 88],            ##calculate total marks for all the three years
[91, 71, 98, 65, 76],
[95, 45, 78, 52, 49]
]
i=0
total=0
count=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        total=total+marks[i][j]
        count=count+1
        average=total/count
        j=j+1
    i=i+1
print("total mark=",total)
print("count=",count)
print("average=",average)