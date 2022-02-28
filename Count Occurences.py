a="Sameer"
i=0
j=0                            ## Occurences
while i<len(a):
    if a[i]=="e":
        j=a[i]
        print(j)
    i=i+1        

#OR


i=0
while i<len(lis):
    if lis[i]=="a":
        c=0
        c=c+1
    i=i+1
    print(lis[i],"=",c)



a="ningthemla"
i=0
while i<len(a):
    if a[i]=="n":                ##Count Occurences
        count=1
        count=count+1
        print(a[i],":",count)
        break
    i=i+1



   
char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=[]
while i<len(char_list):                 ##Count Occurences
    j=0
    count=0
    b=[]
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    b.append(char_list[i])
    b.append(count)
    if b not in a:
        a.append(b)
    i=i+1
print(a)