#DP10_Divisor_Game.py
n=int(input("enter the value of n:"))

def factors(i):
	num=[]
	for j in range(1,i,+1):
		if i%j==0:
			num.append(j)
	return num

my_dict={}

for i in range(1,n+1,+1):
	print("my_dict:",my_dict)
	if i==1:
		my_dict[i]=False
	elif i==2:	
		my_dict[i]=True
	else:
		if i%2==0:
			num=factors(i)
			result=False
			for k in num:
				result=result or (not (my_dict[i-k]))
			my_dict[i]=result
		else:
			my_dict[i]= not(my_dict[i-1])
print(my_dict[n])


