#binarytree23.py
#Construct String from Binary Tree

# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the empty parenthesis pairs. And it will be "1(2(4))(3)".

# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except the () after 2 is necessary to indicate the absence of a left child for 2 and the presence of a right child.

from binarytree1 import build_binarytree,print_binarytree

def constructstring(root,data):
	if root == None:
		return "()"
	else:
		left=constructstring(root.left,data)
		right=constructstring(root.right,data)

		# if root.data==data:
		# 	return root.data+left+right
		# else:
		return "("+root.data+left+right+")"

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
string=constructstring(root,root.data)
print(string)
string=string[1:len(string)-1]
print(string)
result=""
i=0
while(i<len(string)):
	if string[i]=="(" and i+1<len(string) and string[i+1]==")":
		if i+2 < len(string) and string[i+2] == "(":
			if i+3 < len(string) and string[i+3] !=")":
				result=result+string[i]+string[i+1]
				i+=2
				print("3.",result)
			else:
				pass
				print("4.",result)
				i+=1
		elif i+2 < len(string) and string[i+2] == ")":
			pass
			i+=2
			print("2.",result)
	else:
		result=result+string[i]
		i+=1
		print("1.",result)

print(result)




