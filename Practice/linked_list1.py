#linkedlist1.py
# Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B. 
# You should preserve the original relative order of the nodes in each of the two partitions. 
# Input 1: 
# A = [1, 4, 3, 2, 5, 2]
# B = 3
# Input 2: 
# A = [1, 2, 3, 1, 3]
# B = 2
# Output 1: 
# [1, 2, 2, 4, 3, 5]
# Output 2: 
# [1, 1, 2, 3, 3]
# Explanation 1:
# [1, 2, 2] are less than B wheread [4, 3, 5] are greater than or equal to B.
# Explanation 2:
# [1, 1] are less than B wheread [2, 3, 3] are greater than or equal to B.

class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linkedlist:
	def __init__(self):
		self.head=None
	def append(self,data):
		new_node=node(data)

		if not self.head:
			self.head=new_node
			return
		last=self.head
		while last.next:
			last=last.next
		last.next=new_node

	def print(self):
		current=self.head
		while current:
			print(current.data)
			current=current.next

	def rearrange(self,g_ll,l_ll,b):
		current=self.head
		while current:
			if current.data < b:
				l_ll.append(current.data)
			else:
				g_ll.append(current.data)
			current=current.next
	def concat(self,g_ll):
		current=self.head
		if self.head is None:
			self.head=g_ll.head
			return
		while current.next:
			current=current.next
		current.next=g_ll.head


inp=input("enter elements of array sep by spaces:")
A=list(map(int,inp.split()))
b=int(input("enter element based on A is arranges"))

ll=linkedlist()
g_ll=linkedlist()
l_ll=linkedlist()

for i in A:
	ll.append(i)
ll.rearrange(g_ll,l_ll,b)
l_ll.concat(g_ll)
l_ll.print()





