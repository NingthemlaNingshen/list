marks = [
[78, 76, 94, 86, 88],      ###calculate total mark and find out average for each year
[91, 71, 98, 65, 76],
[95, 45, 78, 52, 49]
]
i=0
while i<len(marks):
    j=0
    count=0
    total=0
    while j<len(marks[i]):
        count=count+1
        total=total+marks[i][j]
        average=total/count
        j=j+1
    i=i+1
    print("count of",i,"year is",count)
    print("total of",i,"year is",total) 
    print("average of",i,"year is",average)







