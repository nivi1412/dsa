#binarytree13_.py

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
		def sample(length):
			nonlocal current
			if length <=0:
				return None
			left=sample(length//2)
			root=BT(current.data)
			current=current.next
			root.left=left
			right=sample(length-(length//2)-1)
			root.right=right
			return root
		return sample(length)


ll=linkedlist()
ll.append(-10)
ll.append(-3)
ll.append(0)
ll.append(5)
ll.append(9)
length=ll.length_ll()
root=construct_HBBT(length)
print_binarytree(root)

