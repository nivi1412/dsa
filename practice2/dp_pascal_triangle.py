#DP_Pascal_traingle.py

def pascaltriangle(num,my_dict)->list:
	if num in my_dict:
		return my_dict[num]
	if num==1:
		my_dict[num]=[1]
	elif num==2:
		my_dict[num]=[1,1]
	else:
		my_list=pascaltriangle(num-1,my_dict)
		local=[]
		for i in range(len(my_list)-1):
			local.append(my_list[i]+my_list[i+1])
		local=[1]+local+[1]
		my_dict[num]=local
	return my_dict[num]

num=int(input("enter no of rows"))
# answer=[]

#top down
# for i in range(num+1):
# 	if i==0:
# 		print("enter the num >0")
# 	elif i==1:
# 		answer.append([1])
# 	elif i==2:
# 		answer.append([1,1])
# 	else:
# 		local=[]
# 		for j in range(i-2):
# 			local.append(answer[i-2][j]+answer[i-2][j+1])
# 		local=[1]+local+[1]
# 		answer.append(local)
# print(answer)

#bottom up
my_dict={}
if num==0:
	print("enter the num >0")
else:
	for i in range(1,num+1,+1):
		pascaltriangle(i,my_dict)
print(my_dict.values())