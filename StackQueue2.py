#StackQueue2.py
#print first non repeating character if the char repeasts print 
# Given a string A denoting a stream of lowercase alphabets. You have to make new string B.
# B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found then append '#' at the end of B.
# Input 1:
#  A = "abadbc"
# Input 2:
#  A = "abcabc"
# Output 1:
#  "aabbdd"
# Output 2:
#  "aaabc#"

from collections import deque

Arr=input("enter the string")
if len(Arr)>0:
	char_rep=[0]*26
	q=deque()
	q.append(Arr[0])
	char_rep[ord(Arr[0])-ord('a')]+=1

	j = 0
	for i in range(1,len(Arr),+1):
		char_rep[ord(Arr[i])-ord('a')]+=1
		if char_rep[ord(Arr[j])-ord('a')]<2 :
			q.append(Arr[j])
		else:
			while(j<i):
				j+=1
				if char_rep[ord(Arr[j])-ord('a')]<2 :
					q.append(Arr[j])
					break
				elif i==j and Arr[j] in q :
					q.append("#")
					break
	print(q)
else:
	print("enter the string length > 0")
			



