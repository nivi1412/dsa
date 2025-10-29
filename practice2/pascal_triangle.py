#pascal_triangle.py

numRows=int(input("enter the row count: "))
dp=[]
dp.append([1])

if numRows>=2:
	dp.append([1,1])
	j=3
	while(j<numRows+1):
		local=[]
		for i in range(1,len(dp[-1])):
			local.append(dp[-1][i-1]+dp[-1][i])
		print("local:",local)
		dp.append([1]+local+[1])
		j+=1

print(dp)
print(dp[-1])