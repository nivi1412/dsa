#Heap1.py
# Given N bags, each bag contains Bi chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Bi chocolates, then the magician fills the ith bag with floor(Bi/2) chocolates.
# Find the maximum number of chocolates that kid can eat in A units of time.
# NOTE: 
# floor() function returns the largest integer less than or equal to a given number.
# Return your answer modulo 109+7

# Input 1:
#  A = 3
#  B = [6, 5]
# Input 2:
#  A = 5
#  b = [2, 4, 6, 8, 10]

# Output 1:
#  14
# Output 2:
#  33

import heapq
import math

inp=input("enter the elements seperated by spaces")
B=list(map(int,inp.split()))
A=int(input("enter the time units"))
heap=[]
count=0
for i in B:
	heapq.heappush(heap,i*-1)

for i in range(A):
	j=-heapq.heappop(heap)
	count=count+j
	j=math.floor(j//2)
	heapq.heappush(heap,j*-1)

print(count)

