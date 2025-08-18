#fibonacciseries.py
# def fibonacci(num):
# 	if num==0:
# 		return 0
# 	elif num==1:
# 		return 1
# 	else:
# 		return fibonacci(num-1)+fibonacci(num-2)

# num=int(input("enter the range of febinocci series:"))
# my_list=[]
# for i in range(num):
# 	my_list.append(fibonacci(i))
# print(my_list)

# def fibonacci(num,my_dict):
# 	print(my_dict)
# 	if num in my_dict:
# 		return my_dict[num]
# 	else:
# 		my_dict[num]=fibonacci(num-1,my_dict)+fibonacci(num-2,my_dict)
# 		return my_dict[num]

num=int(input("enter the range of febinocci series:"))
my_dict={}
# my_dict[0]=0
# my_dict[1]=1

for i in range(num):
	if i == 0:
		my_dict[i] = 0
	elif i == 1:
		my_dict[i] = 1
	else:
		my_dict[i] = my_dict[i-1] + my_dict[i-2]
	print(my_dict[i])

# fibonacci(num-1,my_dict)
# for values in my_dict.values():
# 	print(values)