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

from sortedcontainers import SortedList

A=input("Enter Array of elements:")
A=list(map(int,A.split()))
B=int(input("enter the size of window"))

A_len=len(A)
if B<A_len:
	window=SortedList()
	C=[]
	for i in range(A_len):
		window.add(A[i])
		if len(window)==3:
			C.append(window[-1])
			window.remove(A[i-B+1])
	print(C)
else:
	print(max(A))












