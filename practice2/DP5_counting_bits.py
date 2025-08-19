#DP5_counting_bits.py

def binary(i, my_dict):
	count=0
	if(i>0):
		if i in my_dict:
			return my_dict[i]
		if i%2==1:
			count+=1
		count = count+ binary(i//2, my_dict)
	if i not in my_dict:
		my_dict[i]=count
	return count

n=int(input("enter the integer n:"))
my_list=[]
for i in range(n+1):
	my_dict={}
	count=binary(i, my_dict)
	my_list.append(count)
print(my_list)