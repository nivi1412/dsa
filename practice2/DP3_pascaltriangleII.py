##DP3_pascaltriangleII.py
#fetch only the last row value

num=int(input("enter no of rows of pascal traingle:"))
my_dict={}
if num==1:
	my_dict[num]=[1]
elif num==2:
	my_dict[1]=[1]
	my_dict[num]=[1,1]
else:
	my_dict[1]=[1]
	my_dict[2]=[1,1]
	for i in range(3,num+1,+1):
		local=[]
		for j in range(len(my_dict[i-1])-1):
			local.append(my_dict[i-1][j]+my_dict[i-1][j+1])
		local=[1]+local+[1]
		my_dict[i]=local
print(my_dict[num])
