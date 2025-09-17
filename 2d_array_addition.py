#2d array addition

row_len1= int(input("enter no of rows of 1st matrix seperated by spaces:"))
col_len1= int(input("enter no of cols of 1st matrix seperated by spaces:"))

row_len2= int(input("enter no of rows of 2nd matrix seperated by spaces:"))
col_len2= int(input("enter no of cols of 2nd matrix seperated by spaces:"))

A=[]
B=[]
Sum=[[0 for _ in range(row_len1)] for _ in range(col_len1)]

if(row_len1 == row_len2 and col_len1==col_len2):
	for i in range(row_len1):
		print("enter the",i+1,"th row elements of 1st matrix seperated by spaces:")
		inp=input()
		inp=list(map(int,inp.split()))
		A.append(inp)

	for i in range(row_len2):
		print("enter the",i+1,"th row elements of 2nd matrix seperated by spaces:")
		inp=input()
		inp=list(map(int,inp.split()))
		B.append(inp)


	#add 2 arrays


	for i in range(row_len1):
		for j in range(col_len1):
			Sum[i][j]=(A[i][j]+B[i][j])

	for i in range(row_len1):
		for j in range(col_len1):
			print(Sum[i][j])
