#Heap4.py
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]

import heapq
k=int(input("enter number of linkedlists:"))
lists=[]
heap=[]

for _ in range(k):
	inp=map(int,input("enter list:").split)
	lists.append(inp)

for i in lists

