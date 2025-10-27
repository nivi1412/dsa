#DP_Diffwaystoaddparanthesis.py

def addparentheses(expression,memo):
	if expression in memo:
		memo[expression]
	if expression.isdigit():
		return [int(expression)]
	else:
		finallist=[]
		for i in range(1,len(expression),+1):
			if expression[i] in "+-*":
				left=addparentheses(expression[:i],memo)
				right=addparentheses(expression[i+1:],memo)
				print(left,right,expression[i])
				for l in left:
					for r in right:
						if expression[i]=='+':
							finallist.append(int(l)+int(r))
						if expression[i]=='-':
							finallist.append(int(l)-int(r))
						if expression[i]=='*':
							finallist.append(int(l)*int(r))
		print("finallist:",finallist)
		memo[expression]=finallist
		return finallist



expression=input("enter the math expression: ")
memo={}

print(addparentheses(expression,memo))