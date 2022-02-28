num=[2,3,4,7]  ###multiply
i=0
j=1
while i<len(num):
    j=j*num[i]
    i=i+1
print("multiplication of item in list=",j)

list = [6,2,1,2,3] ##multiply
c=[]
i=0
while i<len(list):
    if list[i] not in c:
        c.append(list[i])
    i=i+1
k=0 
Multiple=1
while k<len(c):
    Multiple=Multiple*c[k]
    k=k+1
print(Multiple)



num1=int(input("enter the value="))   ##multiplication 
num=1
while num<=num1:
    i=1
    while i<=10:
        product=num*i
        print(num,"*",i,"=",product)
        i=i+1
    print("")
    num=num+1