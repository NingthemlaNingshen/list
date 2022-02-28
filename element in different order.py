user=int(input("enter your num:"))     ##printing element in order
num=["a",1,"2",5,"b","q"]
i=-user
while i<=-1:
    print(num[i])
    i=i+1

user=int(input("enter your number:"))  ## printing element in reverse order
elements=['a',1,'2',5,'b','q']
i=1
while i<=len(elements):
    print(elements[-i])
    if i==user:
        break
    i=i+1


num=[(2,1),(1,2),(2,9),(4,4),(2,3),(2,5)]  ###ascending order
i=0
while i<len(num):
    j=0
    while j<len(num):
        if num[j][1]>num[i][1]:
            num[i],num[j]=num[j],num[i]
        j=j+1
    i=i+1
print(num)



num=[4,-1,3,6,8,-3,-9,12]    ##printing 0 in negative items
i=0
while i<len(num):
    if num[i]<0 :
        print(0)
    else:
        print(num[i])
    i=i+1

