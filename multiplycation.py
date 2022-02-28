num1=int(input("enter the value="))
num=1
a=[]
while num<=num1:
    i=1
    b=[]
    while i<=10:
        product=num*i
        b.append(product)
        i=i+1
    num=num+1
    a.append(num-1)
    a.append(b)
print(a)