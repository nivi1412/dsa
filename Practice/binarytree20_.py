#binarytree20_.py
#flatternning the binarytree into linkedlist


from binarytree1 import build_binarytree,print_binarytree

def flatterning(root):
	if root!=None:
		if root.left!=None and root.right!=None:
			lf,ll=flatterning(root.left)
			rf,rl=flatterning(root.right)
			print("left,right ele:",lf.data,ll.data,rf.data,rl.data)
			root.left=None
			root.right=lf
			ll.right=rf

			return root,rl
		elif root.left!=None and root.right==None:
			lf,ll=flatterning(root.left)
			root.left=None
			root.right=lf

			return root,ll
		elif root.right!=None and root.left==None:
			rf,rl=flatterning(root.right)
			root.left=None
			root.right=rf

			return root,rl
		else:
			return root,root
	else:
		return None,None

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
rf,rl=flatterning(root)
print_binarytree(rf)