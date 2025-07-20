#binarytree13.py
#Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
from binarytree1 import build_binarytree,print_binarytree
class BT:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

class linkedlist:
	def __init__(self):
		self.head=None

	def append(self,data):
		my_node=node(data)
		current=self.head
		if not self.head:
			self.head=my_node
			return
		while current.next:
			current=current.next
		current.next=my_node
	
	def printll(self):
		current=self.head
		while current:
			print(current.data)
			current=current.next

	def length_ll(self):
		count=0
		current=self.head
		while(current):
			count+=1
			current=current.next
		return count

	def construct_HBBT(self,length):
		current=self.head
		
		def convert(length):
			nonlocal current
			if length<=0:
				return None
			left=convert(length//2)
			root=BT(current.data)
			current=current.next
			right=convert(length-(length//2)-1)
			root.left=left
			root.right=right
			return root
		return convert(length)


		

class node:
	def __init__(self,data):
		self.data=data
		self.next=None



ll=linkedlist()
ll.append(-10)
ll.append(-3)
ll.append(0)
ll.append(5)
ll.append(9)
ll.printll()
length=ll.length_ll()
root=ll.construct_HBBT(length)
print_binarytree(root)

#construct heightbalance binarytree
#A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

length=ll.length_ll()




