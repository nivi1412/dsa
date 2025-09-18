#Dp_Ugly_Number_II_.py
#low time complexity
import heapq

n=int(input("enter the ugly number: "))
i=1
count=1

dp={}
heap=[]

for i in range(1,n+1):
	dp[i]=i
for i in range(7,n+1):
	for j in range(1,i):
		heapq.heappush(heap,2*dp[j])
		heapq.heappush(heap,3*dp[j])
		heapq.heappush(heap,5*dp[j])

	while(1):
		val=heapq.heappop(heap)
		if val>dp[i-1]:
			dp[i]=val
			break

print(dp)
print(dp[n])

