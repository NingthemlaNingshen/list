a=[4,3,41,8,7,21,]  ##maximum number
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
print("largest=",max)

a=[4,3,41,8,7,21,]  ##smallest number in list
i=0
s=a[i]
while i<len(a):
    if a[i]<s:
        s=a[i]
    i=i+1
print("smallest=",s) 


num=[50,40,23,70,56,12,5,10,7]
i=0
a=0
while i<len(num):
    if num[i]>a:
        a=num[i]
    i=i+1
print("max is",a)