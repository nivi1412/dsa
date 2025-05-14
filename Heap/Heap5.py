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

def MedianFinder(commands,inputs,median):
	heap=[]
	heap1=[]
	count=0
	for command,lis in zip(commands,inputs):
		if command=="addNum":
			count+=1
			median.append("null")
			#heapq.heappush(median,"null")
			heapq.heappush(heap1,lis)


		elif command=="findMedian":
			heap=heap1[:]
			heapq.heapify(heap)
			if count%2==0:
				medcount=0
				while heap:
					val=heapq.heappop(heap)
					medcount+=int(val[0])
				#print("str(medcount/2)",medcount/2)
				median.append(float(medcount/2))
				#heapq.heappush(median,str(medcount/2))

			else:
				count=(count//2+1)
				print("count:",count)
				i=0
				while heap:
					i+=1
					if i==count:
						print("i:",i)
						val=heapq.heappop(heap)
						median.append(float(val[0]))
						#heapq.heappush(median,str(val[0]))
					else:
						heapq.heappop(heap)
		else:
			median.append("null")
			#heapq.heappush(median,"null")
			#print(median)

	return median


commands=input("enter the list of command inputs:")
inputs=input("enter the inputs respective to the commands")

commands=ast.literal_eval(commands)
inputs=ast.literal_eval(inputs)
median=[]

for command in commands:
	if command=="MedianFinder":
		median=MedianFinder(commands,inputs,median)

print(commands)
print(inputs)
print(median)




