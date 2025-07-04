#Heap5.py
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

import ast
import heapq

inp=input("enter the commands:")
val=input("enter the value array")
inp=ast.literal_eval(inp)
val=ast.literal_eval(val)
out=[]
lists=[]
count=0
Sum=0



for command,value in zip(inp,val):
	if command=="MedianFinder":
		out.append('null')
	elif command=="addNum":
		heapq.heappush(lists,value[0])
		#lists.append(value[0])
		count+=1
		Sum=Sum+value[0]
		out.append('null')

	elif command=="findMedian":
		if count%2==0:
			print("median:",Sum/count)
			out.append(Sum/count)
		else:
			for i in range(count-1):
				res=heapq.heappop(lists)
			out.append(res)
print(out)


