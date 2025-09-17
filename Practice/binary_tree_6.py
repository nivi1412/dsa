#binarysearch6.py
#find the no of unique binary search trees with given no of nodes

def uniqueBSTcount(node_count):
	if node_count==0 or node_count==1:
		return 1
	else:
		count=0
		for root in range(1,node_count+1):
			left=root-1
			right=node_count-root
			print("l,r:",left,right)
			count=count+(uniqueBSTcount(left)*uniqueBSTcount(right))
		return count

node_count=int(input("enter number of nodes:"))
print(uniqueBSTcount(node_count))