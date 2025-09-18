#DP7_Fibonacci_Number.py

num=int(input("enter the number: "))
my_dict={}
for i in range(num+1):
	if i==0:
		my_dict[i]=0
	elif i==1:
		my_dict[i]=1
	else:
		my_dict[i]=my_dict[i-1]+my_dict[i-2]
		del my_dict[i-2]
print(my_dict)
print(my_dict[num])