a=[31,47,50,21,18,19,78,10,0]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i=i+1
print(a)