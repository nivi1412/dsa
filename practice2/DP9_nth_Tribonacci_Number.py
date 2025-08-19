#DP9_Nth_Tribonacci_Number.py

n=int(input("enter the value of n: "))
k=n-3
my_dict={}
count=0

for i in range(n):
	if i==0:
		my_dict[i]=0
	elif i==1:
		my_dict[i]=1
	elif i==2:
		my_dict[i]=1
	else:
		my_dict[i]=my_dict[i-1]+my_dict[i-2]+my_dict[i-3]
		del my_dict[i-3]
if n>=3:
	count+=my_dict[n-3]+my_dict[n-2]+my_dict[n-1]
	print(count)
else:
	print(my_dict[n-1])