#prefixstring.py
#find prefix string for all the strings given in array

def findprefix(A,length):
	j=0
	jmax=len(A[0])
	result=""
	count=0
	for word in A:
		if(len(word)<jmax):
			jmax=len(word)
	while(j<=jmax-1):
		for i in range(1,length,+1):
			#print("i,j:",i,j)
			if (A[0][j]==A[i][j]):
				#print(A[0][j])
				#print(A[i][j])
				count+=1
			else:
				return result
			if(count==length-1):
				result+=A[0][j]
		count=0
		j+=1
	return result

	

length=int(input("enter length of string array"))
A=[]
prefix=[]
for i in range(length):
	inp=str(input("enter the string"))
	A.append(inp)
prefix.append(findprefix(A,length))
print(prefix[0])






			







