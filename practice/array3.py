#array3.py
#find 2d prefix sum array from the main array
#prefix of 0th row is sum of previous elements along with current element 
#prefix sum of 0 th colum is sum of prev 0th col elements till current element
#prefix sum of remaining elements is PA[i][j]=PA[i-1][j]+PA[i][j-1]+A[i][j]-PA[i-1][j-1]

row=int(input("enter number of rows"))
A=[]


for i in range(row):
	inp=list(map(int,(input("enter row values sep by spaces:").split())))
	A.append(inp)
PA=[[0 for _ in range(row)]for _ in range(len(A[0]))]

PA[0][0]=int(A[0][0])
Sum_row=PA[0][0]
Sum_col=PA[0][0]
for i in range(row):
	for j in range(len(A[0])):
		if (i==0 and j!=0):
			PA[0][j]=PA[0][j-1]+A[0][j]
		elif(i!=0 and j==0):
			PA[i][0]=PA[i-1][0]+A[i][0]
		else:
			PA[i][j]=PA[i-1][j]+PA[i][j-1]+A[i][j]-PA[i-1][j-1]
print(PA)