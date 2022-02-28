magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]] ##magic square
i=0
row=0
column=0
diagonal=0
while i<len(magic_square ):
    row=row+magic_square [i][0]
    column=column+magic_square [i][1]
    diagonal=diagonal+magic_square [i][2]
    i=i+1
print("total sum=",row)
print("total sum=",column)
print("total sum=",diagonal)
if row==column==diagonal:
    print("it is magic square")
else:
    print("it is not magic square")

num=[[8,3,4],
    [1,5,9],
    [6,7,2]]            ##magic square
i=0
sr=0
sc=0
while i<len(num):
    j=0
    sc=sc+num[i][j]
    sr=sr+num[j][i]
    i=i+1
print(sr)
print(sc)
c=0
d=0
f=(len(num)-1)
d1=0
d2=0
while c<len(num):
    d1=d1+num[c][d]
    d2=d2+num[c][f]
    c+=1
    d+=1
    f-=1
print(d1)
print(d2)
if sc==sr==d1==d2:
    print("Magic Square")
else:
    print("Not a magic square")