#math3.py
#FizzBuzz35

num=int(input("enter a number"))
Array=[]
for i in range(1,num+1):
	if i%3==0 and i%5==0:
		Array.append("FizzBuzz")
	elif i%3==0:
		Array.append("Fizz")
	elif i%5==0:
		Array.append("Buzz")
	else:
		Array.append(i)
print(Array)


