i=0
a=[]
b=[]
while i<=10:         ##putting odd or even in the list from 1-10
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
    i=i+1
print("list of even num =",a)
print("list of odd num =",b)

num=[1,2,5,8,3,7,4]
i=0
b=[]
c=[]                   ##putting even and odd in new list
while i<len(num):
    if num[i]%2==0:
        b.append (num[i])
    else:
        c.append(num[i])
    i=i+1
print("list of even num =",b)
print("list of odd num =",c)    

num=[1,2,5,8,3,7,4]
i=0
b=[]
c=[]
even_sum=0
odd_sum=0                   ##putting even and odd in new list and finding their sum
while i<len(num):
    if num[i]%2==0:
        b.append (num[i])
        even_sum=even_sum+(num[i])
    else:
        c.append(num[i])
        odd_sum=odd_sum+(num[i])
    i=i+1
print("list of even num =",b,"sum of even list is=",even_sum)
print("list of odd num =",c,"sum of odd list is=",odd_sum)



num=[11,4,5,3,7,4,2]
i=0
b=[]
c=[]
even_sum=0
odd_sum=0 
even_count=0
odd_count=0                  ##putting even and odd in new list and finding their average
while i<len(num):
    if num[i]%2==0:
        b.append (num[i])
        even_sum=even_sum+(num[i])
        even_count=even_count+1
        even_average=even_sum/even_count
    else:
        c.append(num[i])
        odd_sum=odd_sum+(num[i])
        odd_count=odd_count+1
        odd_average=odd_sum/odd_count
    i=i+1
print("list of even num =",b,"{","sum of even list is=",even_sum,"}")
print("count of even=",even_count,"   ","average of even list=",even_average)
print("list of odd num =",c,"{","sum of odd list is=",odd_sum,"}")
print("count of odd=",odd_count,"   ","average of odd list=",odd_average)




i=0
a=[]
b=[]
while i<=10:
    if i%2==0:
        a.append(i)
    else:
         b.append(i)
    i=i+1
print("list of even num=",a)
print("list of odd num=",b)

