#StackQueue6.py

# An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each string may be an integer or an operator.
# Input 1:
#     A =   ["2", "1", "+", "3", "*"]
# Input 2:
#     A = ["4", "13", "5", "/", "+"]
# Output 1:
#     9
# Output 2:
#     6

A=input("enter the array elements and symbols seperated by space").split()
B=['+','-','*','/']
stack=[]
flag=True
for i in A:
	if i not in B:
		stack.append(i)
	else:
		a=int(stack.pop())
		b=int(stack.pop())
		if i==B[0]:
			c=b+a
		elif i==B[1]:
			c=b-a
		elif i==B[2]:
			c=b*a
		elif i==B[3]:
			if a!=0:
				c=b/a
			else:
				print("error!div by 0")
				flag=False
				break
		stack.append(c)
if flag==True:
	print(stack.pop())
