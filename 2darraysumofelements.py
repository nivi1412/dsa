#find sum of all elemnets in 2d array

row=int(input("enter number of rows:"))
col=int(input("enter number of col:"))

arr=[]

for i in range (row):
	print("enter value of",i+1,"th row seperated by spaces:")
	inp=input()
	rows=list(map(int,inp.split()))
	arr.append(rows)



sum=0
for i in range(row):
	for j in range(col):
		sum=sum+arr[i][j]
	
print("sum of elements:",sum)


