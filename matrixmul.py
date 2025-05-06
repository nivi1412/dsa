#2d array multipl;ication

row_len1=int(input("enter row length of 1st matrix:"))
row_len2=int(input("enter row length of 2nd matrix:"))
col_len1=int(input("enter col length of 1st matrix:"))
col_len2=int(input("enter col length of 2nd matrix:"))

if (col_len1==row_len2):
	A=[]
	B=[]
	C=[[0 for _ in range(row_len1)]for _ in range(col_len2)]

	for i in range(row_len1):
		print("enter ",i+1,"th row values with spaces")
		inp=input()
		inp=list(map(int,inp.split()))
		A.append(inp)

	for i in range(row_len2):
		print("enter ",i+1,"th row values with spaces")
		inp=input()
		inp=list(map(int,inp.split()))
		B.append(inp)

	#multiply
    
	for i in range(row_len1):
		print("i:",i)
		for j in range(col_len2):
			print("j:",j)
			sum=0
			for k in range(row_len2):
				print("k:",k)
				print("row and col values:",A[i][k], B[k][j])
				sum=sum+(A[i][k]*B[k][j])
				print("sum:",sum)

			C[i][j]=sum

	for q in C:
			print(q)