#Heap3.py
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

import heapq
import math
A=int(input("enter the ordered pairs number:"))
k=int(input("enter number of closest points req from origin:"))

point=[]
heap=[]

for _ in range(A):
	x,y=map(int,input("enter x,y:").split())
	point.append([x,y])
for x,y in point:
	heapq.heappush(heap,(math.sqrt(x**2+y**2),[x,y]))

for i in range(k):
	print(heapq.heappop(heap))

