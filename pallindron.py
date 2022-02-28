List=['maam','apple','ibobi','anshika','racecar','','sir'] ##palindrome
i=0
count=0
while i<len(List):
      j=0
      while j< len(List[i]):
          if List[i][0::1]==(List[i][-1::-1]):
              count=count+1
              break
          j=j+1
      i=i+1
print(count)



name=['m','a','a','m'] ##palindrome
i=0
j=0
while i<len(name):
    j=name[-1::-1]
    if (name==j):
        i=i+1
print("name is a palindrome",j)