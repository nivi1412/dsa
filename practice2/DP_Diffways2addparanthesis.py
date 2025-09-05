# DP_Diffways2addparanthesis.py
import ast

def addparentheses(expression,memo)->list:
	if expression in memo:
		return memo[expression]

	if expression.isdigit():
		return [int(expression)]
	else:
		finallist=[]
		for i in range(1,len(expression),+1):
			if expression[i] in "-*+":
				s1=expression[0:i]
				s2=expression[i+1:]
				left=addparentheses(s1,memo)
				right=addparentheses(s2,memo)
				for l in left:
					for r in right:
						if expression[i]=='+':
							finallist.append(l+r)
						if expression[i]=='-':
							finallist.append(l-r)
						if expression[i]=="*":
							finallist.append(l*r)
		memo[expression]=finallist
		return finallist

expression=input("enter the expression:")
memo={}
print("final:",addparentheses(expression,memo))