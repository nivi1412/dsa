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

import ast

A=input("enter inpur expression:")
A=ast.literal_eval(A)
res=0
stack=[]
symbol=["+","-","*","/"]
for i in A:
	if i in symbol:
		a=int(stack.pop())
		b=int(stack.pop())
		if i=="+":
			c=a+b
		elif i=="-":
			c=a-b
		elif i=="*":
			c=a*b
		elif i=="/":
			if a!=0:
				c=b/a
			else:
				print("div error")
		stack.append(c)
	else:
		stack.append(i)
print(c)