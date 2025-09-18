#DP_countingbits.py

# def countbits(i,my_dict):
# 	count=0
# 	if i>0:
# 		if i in my_dict:
# 			return my_dict[i]
# 		if i%2!=0:
# 			count+=1
# 		count=count+countbits(i//2,my_dict)
# 	if i not in my_dict:
# 		my_dict[i]=count
# 	return count


n=int(input("enter the number:"))
my_dict={}
# #top down
# for i in range(1,n+1):
# 	count=countbits(i,my_dict)
# print(my_dict.values())

#bottom up

for i in range(n+1):
	if i==0:
		my_dict[i]=0
	elif i==1:
		my_dict[i]=1
	else:
		count=0
		j=i
		if i%2!=0:
			count+=1
		print("count,my_dict",count,my_dict,i,i//2)
		my_dict[j]=count+my_dict[i//2]

print(my_dict)



