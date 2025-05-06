#StackQueue4.py
# Given an array of integers A.  There is a sliding window of size B which 
# is moving from the very left of the array to the very right. 
# You can only see the w numbers in the window. Each time the sliding window moves 
# rightwards by one position. You have to find the maximum for each window. 
# The following example will give you more clarity.
# The array A is [1 3 -1 -3 5 3 6 7], and B is 3.
# Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].
# Note: If B > length of the array, return 1 element with the max of the array.
# Input 1:
#     A = [1, 3, -1, -3, 5, 3, 6, 7]
#     B = 3
# Output 1:
#     C = [3, 3, 5, 5, 6, 7]


#complexity: O(n*B)
# inp=input("enter the array elements seperated by space")
# A=list(map(int,inp.split()))
# B=int(input("enter the window size"))
# result=[]
# q=[]

# if B>=len(A):
# 	result.append(max(A))
# else:
# 	for a in range(0,len(A)-B+1,+1):
# 		i=A[a]
# 		j=A[a+B-1]
# 		k=a
# 		maxi=min(A)
# 		while(k<(a+B)):
# 			if A[k]>maxi:
# 				maxi=A[k]
# 			k+=1
# 		result.append(maxi)
# print(result)

#complexity: O(nlogn)

from collections import OrderedDict
from sortedcontainers import SortedList

def slidingwindow(A,B):
	if B>len(A):
		return(max(A))

	window=SortedList()
	stack=[]

	for i in range(len(A)):
		window.add(A[i])

		if i>=B-1:
			print(window)
			stack.append(window[-1])
			window.remove(A[i-B+1])
			#window.pop(0)
	return stack

inp=input("enter the array seperated by spaces")
B=int(input("enter the window size"))
nums=list(map(int,inp.split()))

window=[]

result=slidingwindow(nums,B)
print(result)

























