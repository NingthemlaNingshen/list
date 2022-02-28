List=['abc','xyz','aa','aba','1221'] #count similar cha first & last if the string len is 2 or more
i=0
count=0
while i<len(List):
      j=0
      while j< len(List[i]):
          if List[i][0]==(List[i][-1]):
              count=count+1
              break
          j=j+1
      i=i+1
print(count)



##meraki question

num=[50, 40, 23, 70, 56, 12, 5, 10, 7]
count=0
i=0
while i<len(num):
    if num[i]>20:
        count=count+1
    i=i+1
print(count)



numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
while i<len(numbers):
    i=i+1
print("length of the list=",i)

str = input("Enter a string: ")
counter = 0
for i in str:
      counter = counter+1
print("Length of the input string is:", counter)


num = [50, 40, 23, 70, 56, 12, 5, 10,9 ]
count=0
while num[count:]:   
    count=count+1
print(count)

a=[1,2,3,4,5,6,7]
i=0
b=0
count=0
while i<len(a):
    if a[i]%2==0:
        b=a[i]
        count+=1
        print("even of a list=",b)
    i=i+1
print("count of even:",count)




a=[4,5,6,7,8,9,10]      ##difference between list
b=[6,7,8,9,10,11,12]
i=0
j=[]
while i<len(a):
    if a[i] not in b:
        j.append(a[i])
    i=i+1
print(j)

n=[[3,4,],[5,6],[5,7]] ##putting in one list
i=0
a=[]
while i<len(n):
    j=0
    while j<len(n[i]):
        a.append(n[i][j])
        j+=1
    i+=1
print(a)

 