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

path=input("enter the directory")
path=path.split("/")
print(path)
q=deque()
string=''
for i in path:
	if i=="." or i=="":
		pass
	elif i=="..":
		q.pop()
		q.pop()
	else:
		q.append("/")
		q.append(i)
for i in q:
	string=string+i
print(string)


