#StackQueue1.py
#find if paranthesis is balanced

def balanced(Arr):
	stack=[]
	i=0
	while(i<len(Arr)):
		if Arr[i]=="(":
			stack.append(1)
		elif Arr[i]==")":
			if stack:
				stack.pop()
			else:
				return False
		i+=1
	if stack:
		return False
	else:
		return True


Arr=input("enter the string of paranthesis")
stack=balanced(Arr)
if(stack):
	print("balanced")
else:
	print("not balanced")
