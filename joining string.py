a=[["I","a","m"],["t","h","e"],["b","e","s","t"]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j=j+1
    i=i+1
    c="".join(b)
print(c)


charecter=input("enter your charecter:") 
l=list(charecter)         ###string putting in different list
i=0
a=[]
while i<len(l):
    if l[i]>="a"  and l[i]<="z" :
        a.append(l[i])   
    else:
       l. remove(l[i])
    i=i+1
print(a)
