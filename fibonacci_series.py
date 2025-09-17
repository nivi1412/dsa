#fibonacciseries.py

def fibonacci(num,my_dict):
	if num<=1:
		return 1
	if num in my_dict:
		return my_dict[num]

	my_dict[num]=fibonacci(num-1,my_dict)+fibonacci(num-2,my_dict)
	return my_dict[num]

num=int(input("enter the Fibonacci series range"))
my_dict={}
print(fibonacci(num,my_dict))
