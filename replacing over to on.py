mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
j="on"
i=0
while i<len(mainStr):                         #replace over to on
        mainStr=mainStr.replace(subStr,j )
        i=i+1
print(mainStr)


mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
a=mainStr.split(" ")
subStr = "over"
new_st=""
i=0
while i<len(a):
    if a[i]==subStr:
        a.remove(subStr)            #eliminate over
    i=i+1
j=0
while j<len(a):
    print(a[j],end="  ")
    j+=1


mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
a=mainStr.split(" ")
subStr = "on "
new_st=" "
i=0
while i<len(a):
    if a[i]=="over":
        new_st=new_st+subStr        ##replacing over to on
    else:
        new_st=new_st+a[i]+" "
    i+=1
print(new_st)



