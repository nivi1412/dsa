#arraymultiplication.py

row1=int(input("enter the row1 value:"))
row2=int(input("enter the row2 value:"))
col1=int(input("enter the col1 value:"))
col2=int(input("enter the col2 value:"))

Arr1=[]
Arr2=[]
mul=[[0 for _ in range(row1)]for _ in range(col2)]


for _ in range(row1):
	a=input("enter the fitst row value seperated by spaces:")
	Arr1.append(list(map(int,a.split())))
for _ in range(row2):
	a=input("enter the fitst row value seperated by spaces:")
	Arr2.append(list(map(int,a.split())))

if col1==row2:
	for i in range(row1):
		for j in range(col2):
			for k in range(col1):
				mul[i][j]=mul[i][j]+Arr1[i][k]*Arr2[k][j]
print(mul)

