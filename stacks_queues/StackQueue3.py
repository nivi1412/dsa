#StackQueue3.py
# Given a string A representing an absolute path for a file (Unix-style).
# Return the string A after simplifying the absolute path.

# Note:
# In Unix-style file system:
# A period '.' refers to the current directory.
# A double period '..' refers to the directory up a level.
# Any multiple consecutive slashes '//' are treated as a single slash '/'.
# In Simplified Absolute path:
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path doesn't end with trailing slashes '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# The path will not have whitespace characters.

# Input 1:
# A = "/home/"
# Input 2:
# A = "/a/./b/../../c/"

# Output 1:
# "/home"
# Output 2:
# "/c"

from collections import deque


q=deque()
q.append("/")
string=""
inp=input("enter the directory")
inp=inp.split("/")
print(inp)

for i in inp:
	if i=="" or i==".":
		pass
	elif i == "..":
		q.pop()
		q.pop()
	else:
		# st=""
		# local=i.split(" ")
		# for j in local:
		# 	st=st+j
		# print(st)
		q.append(i)
		q.append("/")

if q[-1]=="/":
	q.pop()
for i in q:
	string=string+i
print(string)

# def directory(inp):
# 	for i in range(len(inp)):
# 		if i!=0:
# 			if (inp[i]=="/"):
# 				if(inp[i-1]!="/"):
# 					if (inp[i] != " "):
# 						q.append(inp[i])
# 					if inp[i] ==".":
# 						q.clear()
# 				else:
# 					pass

# 			else:
# 				# Change below logic
# 				if inp[i] != " ":
# 					q.append(inp[i])
# 				if inp[i] ==".":
# 					q.clear()
# 		else:
# 			# Change below logic
# 			if inp[i] != " ":
# 				q.append(inp[i])
# 			if inp[i] ==".":
# 				q.clear()

# 	return q



# q=deque()
# string=""
# j=0
# inp=input("enter the directory")
# q=directory(inp)
# if q[-1]=="/":
# 	q.pop()
# if q[0]!="/":q.appendleft("/")
# for i in q:
# 	string=string+i
# print(string)





