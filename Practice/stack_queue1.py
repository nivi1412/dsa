#StackQueue1.py
#find if paranthesis is balanced

def checkparanthesis(paran):
	stack=[]
	for i in paran:
		if i == "(":
			stack.append(1)
		else:
			if stack:
				stack.pop()
			else:
				return False
	if stack:
		return False
	else:
		return True


paran=input("enter the string of paranthesis")
print(checkparanthesis(paran))
