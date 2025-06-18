#array2.py
#2d array sum of all elements of array

row=int(input("enter no of rows of array:"))
A=[]
for i in range(row):
	inp=input("enter elemnts of row",i+1)
	A.append(inp.split())
Sum=0

for i in range(row):
	for j in rnage(len(A[0])):
		Sum=Sum+A[i][j]
print("sum of elements:",Sum)

