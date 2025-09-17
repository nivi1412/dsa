#binarytree10.py
#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the 
#path equals targetSum.
#9880470859


from binarytree_lib import build_binarytree

def check_path(root,target_sum):
	if root!=None:
		print("data",root.data)
		target_sum=target_sum - int(root.data)
		print(target_sum)
		if target_sum == 0:
			return True
		else:
			return (check_path(root.left,target_sum) or check_path(root.right,target_sum))	
	else:
		return False


inp=input("enter the sorted array seperated by spaces:")
inp=inp.split()
target_sum=int(input("enter the required target_sum:"))

root=build_binarytree(inp)
print(check_path(root,target_sum))


