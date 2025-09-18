#heap1.py
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
num=int(input("enter number of times to choose:"))
inp=input("enter array of elements:")
inp=list(map(int,inp.split()))
heap=[]
count=0

for i in inp:
	heapq.heappush(heap,i*-1)
for i in range(num):
	temp=(heapq.heappop(heap)*-1)
	count=count+temp
	insert=temp//2
	heapq.heappush(heap,insert*-1)
print(count)



