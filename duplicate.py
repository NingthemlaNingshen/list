n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]  ##find duplicate value
i=0
j=[]
while i<len(n):
    if n[i] not in j:
        j.append(n[i])
    i=i+1
print(j)  


a = [10,20,30,20,10,50,60,40,80,50,40] ### omit duplicate value
i=0
j=[]
while i<len(a):
    if a[i] not in j:
        j.append(a[i])
    i=i+1
print(j)

num=[1,2,3,2,4,1,5,6,1,2,24,3] ##making new list for duplicate value
i=0
j=[]
k=[]
while i<len(num):
    if num[i] not in j:
        j.append(num[i])
    else:
        k.append(num[i])
    i=i+1
print(j)
print(k)