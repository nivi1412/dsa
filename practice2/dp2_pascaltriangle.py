#DP2_pascaltriangle.py

num=int(input("enter no of rows of pascal traingle:"))
finallist=[]
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
		local.append(1)
		for j in range(len(my_dict[i-1])-1):
			local.append(my_dict[i-1][j]+my_dict[i-1][j+1])
		local.append(1)
		my_dict[i]=local
for values in my_dict.values():
	finallist.append(values)
print(finallist)




