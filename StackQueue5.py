#StackQueue5.py

# Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
# More formally,
#     G[i] for an element A[i] = an element A[j] such that 
#     j is maximum possible AND 
#     j < i AND
#     A[j] < A[i]
# Elements for which no smaller element exist, consider next smaller element as -1.

# Input 1:
#     A = [4, 5, 2, 10, 8]
# Output 1:
#     G = [-1, 4, -1, 2, 2]
# Explaination 1:
#     index 1: No element less than 4 in left of 4, G[1] = -1
#     index 2: A[1] is only element less than A[2], G[2] = A[1]
#     index 3: No element less than 2 in left of 2, G[3] = -1
#     index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
#     index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
# A = [2, 5, 4, 10, 8]
# G = [-1, 2, 2, 4, 4]
# A = [2, 11, 12, 10, 8]
# G = [-1, 2, 11, 2, 2]

inp=input("enter the array elements seperated by space")
A=list(map(int,inp.split()))
G=[]
stack=[]
for i in range(len(A)):
	if i==0:
		G.append(-1)
		stack.append(A[i])
	else:
		while (len(stack)>=1 and A[i]<stack[-1]):
			stack.pop()
		stack.append(A[i])
		print(stack)
		if len(stack) >= 2:
			if stack[-2]>A[i]:
				G.append(-1)
			else:
				G.append(stack[-2])
		else:
			G.append(-1)
print(G)






# for i in range(len(A)):
# 	if i==0:
# 		G.append(-1)
# 		temp.append(A[i])
# 	else:
# 		if(A[i]<temp[i-1]):
# 			temp[0]=A[i]

# 		if temp[0]!=A[i]:
# 			G.append(temp[0])
# 		else:
# 			G.append(-1)
# print(G)
