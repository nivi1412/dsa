#binarytree2.py

from binarytree_lib import build_binarytree, print_binarytree

def is_equal_trees(p,q):

	if p != None and q!=None:
		print("l:",p.data)
		print("r:",q.data)
		if p.data != q.data:
			return False
		else:
			return is_equal_trees(p.left,q.left) and is_equal_trees(p.right,q.right)

	elif p != None and q == None:
		return False
	elif p==None and q!= None:
		return False
	else:
		print("jello")
		return True

inp1=input("enter the nodes of bin tree:")
inp1=inp1.split()

inp2=input("enter the nodes of bin tree:")
inp2=inp2.split()


p=build_binarytree(inp1)
q=build_binarytree(inp2)


print(is_equal_trees(p,q))




