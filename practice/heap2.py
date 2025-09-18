#Heap2.py
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq

k=int(input("enter which largest num is req:"))
inp=input("enter elemnts of array:")
nums=list(map(int,inp.split()))

heap=[]

for i in nums:
	heapq.heappush(heap,i*-1)

for i in range(k):
	result=-heapq.heappop(heap)

print(k,"th largest number is: ",result)