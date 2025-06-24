#fibonacciseries.py
def fibonocci(num,my_dict):
	if num in my_dict:
		return my_dict[num]
	else:
		# print("one:",fibonocci(num-2,my_dict))
		# print("two:",fibonocci(num-1,my_dict))
		my_dict[num]=fibonocci(num-1,my_dict)+fibonocci(num-2,my_dict)	
		print(my_dict[num])
		return my_dict[num]



num=int(input("enter the range of fib series"))
my_dict={}
if num==1:
	my_dict[1]=0
elif num>=2:
	my_dict[1]=0
	my_dict[2]=1
	fibonocci(num-1,my_dict)

for key,value in my_dict.items():
	print("v:",value)
