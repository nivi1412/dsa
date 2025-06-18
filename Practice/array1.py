#array1.py
#2d array sum of elements

row1=int(input("enter rows of first array"))
row2=int(input("enter rows of second array"))

A=[]
B=[]

for i in range(row1):
	print(i)
	inp=input("enter the values of the row sep by spaces")
	inp=inp.split()
	A.append(inp)

for i in range(row2):
	inp=input("enter the values of the row sep by spaces")
	inp=inp.split()
	B.append(inp)
C=[[0 for _ in range(row1)] for _ in range(len(A[0]))]
for i in range(row1):
	for j in range(len(A[0])):
		C[i][j]=int(A[i][j])+int(B[i][j])

print(C)





