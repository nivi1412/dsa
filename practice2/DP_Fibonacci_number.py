# DP_Fibonacci_number.py

def fibnum(n,my_dict)->int:
	if n in my_dict:
		return my_dict[n]
	my_dict[n]=fibnum(n-1,my_dict)+fibnum(n-2,my_dict)
	return my_dict[n]

n=int(input("enter a num:"))
my_dict={}
# #bottoms up
# for i in range(n+1):
# 	if i==0:
# 		my_dict[i]=0
# 	elif i==1:
# 		my_dict[i]=1
# 	else:
# 		my_dict[i]=my_dict[i-1]+my_dict[i-2]

# print(my_dict[n])

#top down
my_dict[0]=0
my_dict[1]=1
print(fibnum(n,my_dict))
