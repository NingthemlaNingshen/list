a=["a","b",["c",["d","e"],["j","g"],"k"],"l","m","n"]
i=0
b=[]
while i<len(a):
	if type(a[i])==type([]):
		j=0
		while j<len(a[i]):
			if type(a[i][j])==type([]):
				k=0
				while k<len(a[i][j]):
					b.append(a[i][j][k])
					k+=1
			else:
				b.append(a[i][j])
			j+=1
	else:
		b.append(a[i])
	i+=1
print(b)




a=[1,2,[3,[4,5],[6,7],8],9,10,11]
i=0
b=[]
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    b.append(a[i][j][k])
                    k=k+1
            else:
                b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    c=0
    sum=0
    while c<len(b):
        sum=sum+b[c]
        c=c+1
    i=i+1
print(b)
print(sum)




a=[1,2,[3,4,5],[6,7,8]]
i=0
b=[]
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    c=0
    sum=0
    while c<len(b):
        sum=sum+b[c]
        c+=1
    i=i+1
print(b)
print(sum)


