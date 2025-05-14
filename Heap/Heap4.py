#Heap4.py
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]

import heapq

k=int(input("enter number of linkedlists"))
lists=[]
heap=[]
out=[]

for i in range(k):
	ll=input("enter elements of linked list")
	lists.append(list(map(int,ll.split())))

# for i in range(len(lists)):
# 	for j in range(len(lists[i])):
# 		heapq.heappush(heap,lists[i][j])

# length=len(heap)
# for i in range(length):
# 	heapq.heappush(out,(heapq.heappop(heap)))

# print(out)


for i,ll in enumerate(lists):
	if ll:
		heapq.heappush(heap,(ll[0],i,0))
while heap:
	val,ll_index,element_index=heapq.heappop(heap)
	print(val,end=" ")

	if element_index+1<len(lists[ll_index]):
		new_val=lists[ll_index][element_index+1]
		heapq.heappush(heap,(new_val,ll_index,element_index+1))
print()
