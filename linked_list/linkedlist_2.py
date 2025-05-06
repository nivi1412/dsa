# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

class Node():
	def __init__(self,data):
		self.data=data
		self.next=None

class linkedlist():
	def __init__(self):
		self.head=None

	def append(self,data):
		new_node=Node(data)
		current=self.head
		if self.head is None:
			self.head=new_node
			return
		while current.next:
			current=current.next
		current.next=new_node
		return

	def print(self):
		current=self.head
		while current:
			print(current.data,end="->")
			current=current.next
		print("None")

	def remove(self,dll):
		current=self.head
		if self.head is None:
			return
		elif current.next is None:
			dll.append(current.data)
			return
		else:
			prev=current
			current=current.next
			while current:
				if prev.data!=current.data:
					print(prev.data)
					print(current.data)
					dll.append(prev.data)
				else:
					local=current.data
					if current.next is None:
						return
					current=current.next
					while (current.next is not None) and (current.data==local):
						current=current.next

				
				if (current.next is None) and (prev.data!=current.data):
					print("cd:",current.data)
					dll.append(current.data)
					return
				prev=current
				current=current.next


inp=input("enter the values of linked list")
A=list(map(int,inp.split()))
ll=linkedlist()
for i in A:
	ll.append(i)
dll=linkedlist()
ll.remove(dll)
dll.print()
#ll.print()














