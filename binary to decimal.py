num=[1,0,0,1,1,0,1,1]
d=0                  
i=-1
sum=0
while i>=-len(num):
    sum=sum+num[i]*2**d
    d=d+1
    i=i-1
print(sum)


num=[0,0,0,0,1,1,1,1]
d=0
i=-1
sum=0
while i>= -len(num):
    sum=sum+num[i]*2**d
    d=d+1
    i=i-1
print(sum)