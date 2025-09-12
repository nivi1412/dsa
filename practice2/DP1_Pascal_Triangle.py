#DP1_Pascal_Triangle.py

numRows=int(input("enter the row count: "))
my_list=[[1]]
my_list.append([1,1])

for i in range(1,numRows-1):
	local=[1]
	for j in range(1,len(my_list[i])):
		local.append(my_list[i][j-1]+my_list[i][j])
	local.append(1)
	my_list.append(local)

print(my_list)