#array6.py
#2d array matrix multiplication

row_A=int(input("enter row count of matrix A:"))
row_B=int(input("enter row count of matrix B:"))

A=[]
B=[]

for i in range(row_A):
	A.append(list(map(int,input("enter elements of rowA :").split())))
for j in range(row_B):
	B.append(list(map(int,input("enter elements of rowB :").split())))
C=[[0 for _ in range(row_A)] for _ in range(len(B[0]))]
print(C)
Sum=0

if row_A==len(B[0]):
	for i in range(row_A):
		for j in range(len(B[0])):
			for k in range(row_B):
				Sum=Sum+(A[i][k]*B[k][i])

			C[i][j]=Sum
			Sum=0

print(C)

