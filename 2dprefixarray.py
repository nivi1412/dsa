#2d prefix array

row=int(input("enter number of rows:"))
col=int(input("enter number of cols:"))

arr=[]
prearr=[]


for i in range(row):
	print("enter",i+1,"th row values seperated by spaces: ")
	inp=input()
	rows=list(map(int,inp.split()))
	arr.append(rows)
	prearr.append([0]*len(rows))
print(prearr)

prearr[0][0]=arr[0][0]

for k in range(row):
	for l in range(col):

		if(k==0 and l!=0):
			prearr[k][l]=prearr[0][l-1]+arr[0][l]

		elif(l==0 and k!=0):
			prearr[k][l]=prearr[k-1][0]+arr[k][0]

		else:
			prearr[k][l]=prearr[k-1][l]+prearr[k][l-1]-prearr[k-1][l-1]+arr[k][l]

print(prearr)
				
	


